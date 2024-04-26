# Brute Force Solution
# Time Complexity is O(n) + O(n/2)
# Space Complexity is O(n)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        for i in range(len(nums)):
            if nums[i] > 0:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        for i in range(len(arr1)):
            nums[2*i] = arr1[i]
            nums[2*i+1] = arr2[i]
        return nums
# Optimal Solution using Two Pointer
# Time Complexity is O(n)
# Space Complexity is O(n)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_index = 0
        negative_index = 1
        ans = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i]<0:
                ans[negative_index] = nums[i]
                negative_index += 2
            else:
                ans[positive_index] = nums[i]
                positive_index += 2
        return ans

