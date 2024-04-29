# Brute Force Solution
# Time Complexity: O(n^2)
# Space Compolexity is : O(1)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            sum = nums[i]
            for j in range(i+1, len(nums)):
                sum += nums[j]
                if sum%k == 0:
                    return True
        return False
# Optimal Solution Uisng HashMap
# Time Complexity is O(n)
# Space Complexity is O(n)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashMap = {0 : -1}
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            remainder = current_sum % k
            if remainder not in hashMap:
                hashMap[remainder] = i
            elif i - hashMap[remainder] > 1:
                    return True
        return False
               