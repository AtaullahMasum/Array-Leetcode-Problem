# Solution 1
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            correct_index = nums[i] - 1
            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i+1:
                return nums[i]
# Solution 2
# Using Slow and Fast pointer
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
#using Hash Set
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return num
            hashSet.add(num)
   