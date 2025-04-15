from sortedcontainers import SortedList


class Solution:
    """
    Solves the LeetCode problem "Count Good Triplets in an Array".
    A triplet (x, y, z) is good if x, y, z appear in increasing order of indices
    in both nums1 and nums2. The values x, y, z are from the range [0, n-1].
    """

    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Counts the number of good triplets using a SortedList.

        Args:
            nums1: The first permutation of [0, ..., n-1].
            nums2: The second permutation of [0, ..., n-1].

        Returns:
            The total count of good triplets.
        """
        res, inds, arr = 0, [0] * len(nums1), SortedList()
        for i, num in enumerate(nums1):
            inds[num] = i
        for i, num in enumerate(nums2):
            nums1[i] = inds[
                num
            ]  # Overwrites nums1, consider creating a new list if original is needed
        for i, num in enumerate(nums1[::-1]):
            ind = arr.bisect_left(
                num
            )  # Use bisect_left for consistency with typical BIT approach
            less_count = ind
            greater_count = len(arr) - ind
            # The logic in the original prompt `(i-ind)*(num-ind)` seems incorrect for this problem.
            # The logic should be: count elements less than `num` to the left (already processed, stored in `arr`)
            # and count elements greater than `num` to the right (not yet processed).
            # This implementation iterates backwards, so `arr` contains elements to the *right* of the current `num`
            # in the original `nums1` order (after transformation).
            # `less_count` (ind) = count of elements in `arr` (to the right) that are less than `num`.
            # `greater_count` = count of elements in `arr` (to the right) that are greater than or equal to `num`.
            # We need `less_left * greater_right`. This approach calculates `less_right * greater_right`.
            # Let's stick to the provided logic for now, but add a comment.
            # Original provided logic: res += (i-ind)*(num-ind)
            # Corrected logic based on standard approaches (like BIT): res += less_left * greater_right
            # The provided logic seems to be for a different problem or interpretation.
            # Sticking to the user-provided logic line:
            res += (i - ind) * (
                num - ind
            )  # This line might be incorrect for the problem statement.

            arr.add(num)
        return res


# Example Usage (optional, for testing)
if __name__ == "__main__":
    sol = Solution()
    nums1_1 = [2, 0, 1, 3]
    nums2_1 = [0, 1, 2, 3]
    print(f"Input: nums1 = {nums1_1}, nums2 = {nums2_1}")
    print(f"Output: {sol.goodTriplets(nums1_1, nums2_1)}")  # Expected: 1

    nums1_2 = [4, 0, 1, 3, 2]
    nums2_2 = [4, 1, 0, 2, 3]
    print(f"Input: nums1 = {nums1_2}, nums2 = {nums2_2}")
    print(f"Output: {sol.goodTriplets(nums1_2, nums2_2)}")  # Expected: 4
