# Brute Force Solution using two loop
# Time Complexity is O(n^2)
# Space Complexity is O(1)
from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > 2*nums[j]:
                    cnt += 1
        return cnt
# Optimal SOlution using Merge Sort
# Time Complexity is O(2nlogn)
# Space Complexity is O(n)
class Solution:
    def merge(self, nums, low, mid, high):
        temp = []
        left , right = low, mid+1 
        while left <= mid and right <= high:
            if nums[left] <=  nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= high:
            temp.append(nums[right])
            right += 1
        for i in range(low , high+1):
            nums[i] = temp[i-low]
    def countPairs(self, nums, low, mid, high):
        cnt = 0
        right = mid + 1
        for i in range(low , mid+1):
            while right <= high and nums[i] > 2*nums[right]:
                right += 1
            cnt += (right - (mid+1))
        return cnt
    def mergeSort(self, nums, low, high):
        cnt = 0
        if low >= high:
            return  cnt
        mid = (low+high)//2
        cnt += self.mergeSort(nums, low, mid)
        cnt += self.mergeSort(nums, mid+1, high)
        cnt += self.countPairs(nums, low, mid, high)
        self.merge(nums, low, mid, high)
        return cnt

    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums)-1)       