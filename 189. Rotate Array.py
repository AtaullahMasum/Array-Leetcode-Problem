# Solution 1 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        temp = []
        n = len(nums)
        k = k%n
        for i in range(n-k, n):
            temp.append(nums[i])
        for i in range(n - k - 1, -1, -1):
            nums[i+k] = nums[i]
        for i in range(k):
            nums[i] = temp[i]
# Solution 2
class Solution:
    def reverse(self, nums, left, right):
        while left < right:
            nums[left] , nums[right] = nums[right], nums[left]
            left += 1
            right -=1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        self.reverse(nums, 0,n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)