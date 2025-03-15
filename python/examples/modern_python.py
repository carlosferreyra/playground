import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class User:
    name: str
    age: int
    skills: List[str]

    def is_adult(self) -> bool:
        return self.age >= 18


class DataProcessor:
    def __init__(self, data_path: Path) -> None:
        self.data_path = data_path

    def process_users(self, users: List[User]) -> Dict[str, List[str]]:
        """
        Process users and return a mapping of adult status to user names
        """
        result: Dict[str, List[str]] = {"adults": [], "minors": []}

        for user in users:
            try:
                category = "adults" if user.is_adult() else "minors"
                result[category].append(user.name)
            except Exception as e:
                logger.error(f"Error processing user {user.name}: {e}")

        return result

    def find_user_by_skill(self, users: List[User], skill: str) -> Optional[User]:
        """
        Find the first user with a specific skill
        """
        return next((user for user in users if skill in user.skills), None)
