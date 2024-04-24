# Brute Force Solution
# Time Complexity is O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1,-1]
# Better Solution Hashing Solution
# Time Complexity is O(n)
# Space Complexity is O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                return [hashMap[target-nums[i]], i]
            hashMap[nums[i]] = i
        return [-1, -1]
