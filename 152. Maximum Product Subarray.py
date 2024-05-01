# Brute Force Approch using Three Loop
# Time Complexity is O(n^3)
# Space Complexity is O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        maxi = float('-inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                product = 1
                for k in range(i, j+1):
                    product *= nums[k]
                    if product > maxi:
                        maxi = product
        return maxi
               
# Better Solution Using Two Loop
# Time complexity is O(n^2)
# Space Complexity is O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        maxi = float('-inf')
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                if product > maxi:
                    maxi = product             
        return maxi
# Optimal Solution using prefix and sufix
# Time Complexity is O(n)
# Space Complexity is O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
       maxi = float('-inf')
       prefix = 1
       sufix = 1
       n = len(nums)
       for i in range(n):
          if prefix == 0:
             prefix = 1
          if sufix == 0:
             sufix = 1
          prefix *= nums[i]
          sufix *= nums[n-i-1]
          maxi = max(maxi, prefix, sufix)
          
       return maxi