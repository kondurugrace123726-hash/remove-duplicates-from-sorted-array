"""
Problem: Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place 
such that each unique element appears only once.

Return the number of unique elements.

Approach:
- Use two pointers.
- Pointer 'i' tracks the last unique element.
- Pointer 'j' scans through the array.
- When a new unique value is found, increment 'i' and update nums[i].

Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
if __name__ == "__main__":
    solution = Solution()
    nums = [0, 0, 1, 1, 2, 2, 3, 3, 4]
    k = solution.removeDuplicates(nums)
    print("Number of unique elements:", k)
    print("Modified array:", nums[:k])
