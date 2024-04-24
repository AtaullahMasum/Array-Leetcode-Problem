# Brute Force Approch
# Time Complexity is O(n)
# Space Complexity is O(n)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])
        for i in range(len(temp)):
            nums[i] = temp[i]
        remain = len(temp)
        for i in range(remain, len(nums)):
            nums[i] = 0
# Optimal Solution
# Time Complexity is O(n)
# Space Complexity is O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
            