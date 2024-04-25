# Brute Force Solution
# Time Complexity is O(n^2)
# Space Complexity is O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                maxSum = max(maxSum, sum)
        return maxSum
