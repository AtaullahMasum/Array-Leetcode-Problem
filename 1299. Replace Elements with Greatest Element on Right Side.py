class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        maxi = -1
        ans = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > maxi:
                ans.append(maxi)
                maxi = nums[i]
            else:
                ans.append(maxi)
        ans = ans[::-1]
        return ans
        