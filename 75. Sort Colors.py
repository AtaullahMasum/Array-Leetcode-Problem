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
# Optimal Solution Using Dutch National Flag
# Time Complexity is O(n)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low , mid , high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid] , nums[high] = nums[high], nums[mid]
                high -= 1
       
