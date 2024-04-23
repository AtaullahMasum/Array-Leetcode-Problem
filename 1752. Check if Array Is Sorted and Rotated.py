# Time Complexity is O(n)
# Space Complexity is O(1)
class Solution:
    def check(self, nums: List[int]) -> bool:
        rotate, n = 0, len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                rotate += 1
            if rotate > 1:
                return False
        return True