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
#Using natural number formula
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n*(n+1)//2 
        nums_sum = sum(nums)
        return total_sum - nums_sum
# Using Bitwise xor 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       xor1 = 0
       xor2 = 0
       n = len(nums)
       for i in range(n):
          xor1 = xor1 ^ nums[i]
          xor2 = xor2 ^(i+1)
    
       return xor1^xor2

        