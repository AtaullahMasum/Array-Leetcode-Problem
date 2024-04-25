# Brute Force 
# Time Complexity is O(n^2)
# Space Complexity is O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            cnt = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    cnt += 1
            if cnt > n//2:
                return nums[i]
# Better Approch using Sorting
# Time Complexity is O(nlogn)
# Space Complexity is O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        target =nums[n//2]
        return target
# Better Approch using Sorting
# Time Complexity is O(n)
# Space Complexity is O(n//2)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1
        for key, value in hashMap.items():
            if value > n//2:
                return key
# Optimal Solution Using Moore's Voting Algorithm
# Time Complexity is O(n)
# Space Complexcity is O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 1
        element = nums[0]
        for i in range(1,len(nums)):
            if cnt == 0:
                cnt = 1
                element = nums[i]
            elif nums[i] == element:
                cnt += 1
            else:
                cnt -= 1
        return element
        # check for element is majority or not
        count = 0
        for i in range(len(nums)):
            if nums[i] ==element:
                count += 1
        if count > len(nums)//2:
            return element
        else:
            return -1

