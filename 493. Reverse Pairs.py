# Brute Force Solution using two loop
# Time Complexity is O(n^2)
# Space Complexity is O(1)
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > 2*nums[j]:
                    cnt += 1
        return cnt
        