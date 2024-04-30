# Brute Force Solution
# Time Complexity is : O(n) + O(nlogn)
# Space Complexity is : O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.append(num**2)
        result.sort()
        return result
# Optimal Solution 
# Time Complexity is : O(n)
# Space Complexity is : O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        left = 0
        while left < n and nums[left] < 0:
            left += 1
        right = left
        left = left - 1
        while left >= 0 and right < n:
            if nums[left]**2 > nums[right]**2:
                result.append(nums[right]**2)
                right += 1
            else:
                result.append(nums[left]**2)
                left -= 1
        while left >= 0:
            result.append(nums[left]**2)
            left -= 1
        while right < n:
            result.append(nums[right]**2)