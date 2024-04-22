# Using Cyclic Sort
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        i, n = 0, len(nums)
        while i < n:
            correct_index = nums[i] - 1
            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                ans.append(nums[i])
        return ans
# Solution 2
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                ans.append(index+1)
            else:
                nums[index] = -1*nums[index]
        return ans
        
# Solution 3
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        hashSet = set()
        for num in nums:
            if num in hashSet:
                ans.append(num)
            hashSet.add(num)
        return ans