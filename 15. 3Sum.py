# Brute Force Solution
# Time Complexity is O(n^3)
# Space Complexity is O(n)
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