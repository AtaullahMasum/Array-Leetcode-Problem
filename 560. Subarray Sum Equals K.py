# Brute Force Solution
# Time Complexity is O(n^3)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum = 0
                for l in range(i, j+1):
                    sum += nums[l]
                if sum == k:
                    cnt += 1
        return cnt
# Better Solution 
# Time Complexity is O(n^2)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    cnt += 1
        return cnt