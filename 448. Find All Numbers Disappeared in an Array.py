class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n , i = len(nums), 0
        ans = []
        while i < n:
            correct_index = nums[i] - 1
            if  nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans
        