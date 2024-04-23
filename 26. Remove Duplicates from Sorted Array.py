# Brute Force Approach
# Time Complexity is = O(n)+O(2m)+O(mlogm) = O(n) + O(mlogm)
# Space O(m)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_element = set(nums) # O(n)
        unique_element = list(unique_element) #O(m)
        unique_element.sort() # O(mlogm)
        for i in range(len(unique_element)): # O(m)
            nums[i] = unique_element[i]
        return len(unique_element)
# Optimal Solution using two pointer
# Time Complexity is O(n)
# Space Complexity O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
        return i + 1

        