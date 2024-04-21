# Using Cyclic Sort
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n, i = len(nums) , 0
        while i < n:
            correct_index = nums[i]
            if nums[i] < n and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i:
                return i
        return n
        