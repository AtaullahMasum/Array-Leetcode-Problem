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
# Better Solution 
#  Time Compelxity is O(nlogn) + O(n)
# Space Complexity is O(1)
class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest = 1
        lastSmaller = float('inf')
        cnt = 0
        for i in range(len(nums)):
            if nums[i] - 1 == lastSmaller:
                cnt += 1
                lastSmaller = nums[i]
            elif nums[i] != lastSmaller:
                cnt = 1
                lastSmaller = nums[i]
            longest = max(longest, cnt)
        return longest
        
# Optimal Solution 
# Time Compelxity is O(2n)
# Space Compelxity is O(n)
class Solution:  
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums_set:
                current_num = num
                current_length = 1
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_length += 1
                longest = max(longest, current_length)
        return longest