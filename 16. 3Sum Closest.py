# Optimal Solution using two pointer Approch
# Time Complexity: O(nlogn+n^2)
# Space Complexity: O(1)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closestSum = float('inf')
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right  = i+1, n-1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(closestSum - target):
                    closestSum = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                elif current_sum == target:
                    return target
        return closestSum
        