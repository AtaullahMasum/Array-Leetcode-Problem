# Brute Force 
# Time Complexity is O(n^2)
# Space Complexity is O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            cnt = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    cnt += 1
            if cnt > n//2:
                return nums[i]
# Better Approch using Sorting
# Time Complexity is O(nlogn)
# Space Complexity is O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        target =nums[n//2]
        return target
# Optimal Solution 
# Time Complexity is O(n)
# Space Complexcity is O(1)
