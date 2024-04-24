# Brute Force
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
# Better Solution
#  Time Complexity is O(n) + O(n)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        for num in  nums:
            if num == 0:
                cnt0 += 1
            elif num == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        for i in range(cnt0):
            nums[i] = 0
        for i in range(cnt1):
            nums[cnt0+i] = 1
        for i in range(cnt2):
            nums[cnt0+cnt1+i] = 2