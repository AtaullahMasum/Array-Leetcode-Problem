# Brute Force Solution 
# Time Complexity is : O(m+n)
# Space Complexity is : O(m+n)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = [0]*(m+n)
        left, right , index = 0,0,0
        while left < m and right < n:
            if nums1[left] <= nums2[right]:
                nums3[index] = nums1[left]
                left += 1
                index += 1
            else:
                nums3[index] = nums2[right]
                right += 1
                index += 1
        while left < m:
            nums3[index] = nums1[left]
            left += 1
            index += 1
        while right < n:
            nums3[index] = nums2[right]
            right += 1
            index += 1
        for i in range(m+n):
            nums1[i] = nums3[i]
            