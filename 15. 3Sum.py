# Brute Force Solution
# Time Complexity is O(n^3) or O(n^3logn)
# Space Complexity is O(2n)
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        Set = set()
        temp = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 :
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        temp_tuple = tuple(temp)
                        if temp_tuple not in Set:
                            Set.add(temp_tuple)
                            ans.append(temp)
        return ans
    
# Better Solution Using Hashing
# Time Complexity is O(n^2) or O(n^2logn)
# Space Complexity is O(n) + O(2*no. of triplets)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        result = []
        Set = set()
        for i in range(len(nums)):
            hashSet = set()
            for j in range(i+1, len(nums)):
                if -(nums[i]+nums[j]) in hashSet:
                    temp = [nums[i], nums[j],-(nums[i]+nums[j])]
                    temp.sort()
                    temp_tuple = tuple(temp)
                    if temp_tuple not in Set:
                        result.append(temp)
                        Set.add(temp_tuple)
                hashSet.add(nums[j])
        return result
# Optimal Solution Using Two Pointers
# Time Complexity is O(n*logn) + O(n^2)
# Space Complexity is O(no. of Triplets)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        for i in range (len(nums)):
            # Skip duplicates for the fixed element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Use two pointers approach for the remaining elements
            left, right = i + 1, n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0: 
                    left += 1
                elif total > 0:
                    right -= 1
                elif total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                     # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -=1
        return result
