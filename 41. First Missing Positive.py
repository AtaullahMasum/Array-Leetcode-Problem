# Using Cyclic Sort
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i , n = 0, len(nums)
        while i < n:
            correct_index = nums[i] - 1
            if 0 < nums[i] < n and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n+1
# Using HashSet
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        num = 1
        while num in hashSet:
            num += 1
        return num
            