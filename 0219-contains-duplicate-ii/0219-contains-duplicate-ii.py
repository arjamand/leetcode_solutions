class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_indices = {}  # Dictionary to store the indices of each element

        for i, num in enumerate(nums):
            # If the element is already present in the dictionary
            # and the difference between current and previous index is at most k
            if num in num_indices and abs(i - num_indices[num]) <= k:
                return True
            num_indices[num] = i  # Update the index of the element

        return False
