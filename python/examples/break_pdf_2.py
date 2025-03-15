import hashlib
import json
import os
from typing import Callable, Dict, Optional, Union

import PyPDF2

# Use a variable for PDF path instead of hardcoded value
PDF_PATH = ""  # This should be filled by the caller


# Cache handling
def get_cache_path(pdf_path: str) -> str:
    """Generate a unique cache file path based on the PDF's path and file hash"""
    pdf_name = os.path.basename(pdf_path)
    # Use file hash to make sure the cache is tied to a specific PDF file
    file_hash = ""
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            file_hash = hashlib.md5(f.read(8192)).hexdigest()[
                :10
            ]  # Just use the first 8KB for speed

    cache_dir = os.path.join(os.path.expanduser("~"), ".pdf_password_cache")
    os.makedirs(cache_dir, exist_ok=True)
    return os.path.join(cache_dir, f"{pdf_name}_{file_hash}_cache.json")


def load_password_cache(pdf_path: str) -> Dict[str, Union[bool, str]]:
    """Load the password cache for a specific PDF file"""
    cache_path = get_cache_path(pdf_path)
    if os.path.exists(cache_path):
        try:
            with open(cache_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}


def save_password_cache(
    pdf_path: str, password_cache: Dict[str, Union[bool, str]]
) -> None:
    """Save the password cache for a specific PDF file"""
    cache_path = get_cache_path(pdf_path)
    with open(cache_path, "w") as f:
        json.dump(password_cache, f)


def try_password_range(
    reader: PyPDF2.PdfReader,
    callback: Callable[[str], None],
    pdf_path: str,
    start_num: int = 0,
    end_num: int = 99_999_999,
) -> Optional[str]:
    """
    Attempt to brute-force the password of an encrypted PDF file using a specific range of 8-digit numbers.

    Args:
        reader: PyPDF2 PdfReader object
        callback: Function to call with the current password attempt
        pdf_path: Path to the PDF file for caching purposes
        start_num: Starting number in the range (inclusive)
        end_num: Ending number in the range (exclusive)

    Returns:
        The password if found, None otherwise
    """
    # Load cached password attempts
    password_cache = load_password_cache(pdf_path)
    if "successful_password" in password_cache:
        password = password_cache["successful_password"]
        print(f"Using cached password: {password}")
        return password

    # Try numbers in the specified range
    total_attempts = end_num - start_num
    last_save = 0
    save_frequency = 100  # Save every 100 attempts

    for current_num in range(start_num, end_num):
        password = str(current_num)

        # Skip passwords we've already tried
        if password in password_cache and not password_cache[password]:
            continue

        # Progress tracking
        if (current_num - start_num) % 1000 == 0:
            progress = (current_num - start_num) / total_attempts * 100
            print(
                f"Progress: {progress:.2f}% ({current_num - start_num}/{total_attempts})"
            )

        callback(password)
        result = reader.decrypt(password)

        # Cache the result
        password_cache[password] = bool(result)

        # Periodically save the cache
        if len(password_cache) - last_save >= save_frequency:
            save_password_cache(pdf_path, password_cache)
            last_save = len(password_cache)

        if result:
            # Save the successful password
            password_cache["successful_password"] = password
            save_password_cache(pdf_path, password_cache)
            return password

    # Save the final cache state
    save_password_cache(pdf_path, password_cache)
    return None


def main(pdf_path: str) -> Optional[str]:
    """
    Main function to attempt breaking a PDF password.

    Args:
        pdf_path: Path to the PDF file

    Returns:
        The password if found, None otherwise
    """
    global PDF_PATH
    PDF_PATH = pdf_path

    print(f"Attempting to break PDF at: {PDF_PATH}")
    try:
        with open(PDF_PATH, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            if not reader.is_encrypted:
                print("The PDF is not encrypted.")
                return None

            print("The PDF is encrypted.")
            # Attempt to decrypt with an empty password first
            try:
                if reader.decrypt(""):
                    print("Decryption successful with an empty password.")
                    return ""
            except Exception:
                pass

            try:
                print("Trying 8-digit passwords in range 16,400,000 to 16,500,000...")
                password = try_password_range(
                    reader,
                    lambda x: print(f"Trying: {x}"),
                    pdf_path=PDF_PATH,
                    start_num=0,
                    end_num=100_000_000,
                )

                if password:
                    print(f"Password found: {password}")
                    return password
                else:
                    print("Password not found within the specified range.")
                    return None
            except Exception as e:
                print(f"Decryption failed: {e}")
                return None
    except FileNotFoundError:
        print(f"Error: File not found at {PDF_PATH}")
        return None
    except PermissionError:
        print(f"Error: No permission to read file at {PDF_PATH}")
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        # Default path if none provided
        home = os.path.expanduser("~")
        pdf_path = f"{home}/Downloads/pdf.pdf"

    main(pdf_path)
