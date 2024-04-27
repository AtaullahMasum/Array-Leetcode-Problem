# Brute Force Solution
# Time Complexity is O(n^2)
# Space Complexity is O(1)
class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return True
        return False
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        for i in range(len(nums)):
            cnt = 1
            x = nums[i]
            while self.linearSearch(nums, x+1):
                cnt += 1
                x = x+1
            if longest < cnt:
                longest = cnt
        return longest
        