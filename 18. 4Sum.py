# Brute Force Solution using four Loop
# Time Complexity: O(n^4)
# space complexity : O(2* no. of quadruplets)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        hashSet = set()
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    for l in range(k+1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            temp = [nums[i] , nums[j] , nums[k] , nums[l]]
                            temp.sort()
                            temp_tuple = tuple(temp)
                            if temp_tuple not in hashSet:
                                result.append(temp)
                                hashSet.add(temp_tuple)
        return result
# Better Solution using Hashing
# Time Complexity: O(n^3)
# space complexity : O(2* no. of quadruplets)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        Set = set()
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                hashSet = set()
                for k in range(j+1, len(nums)):
                   remain = target - (nums[i] + nums[j] + nums[k])
                   if remain in hashSet:
                      temp = [nums[i], nums[j], nums[k], remain]
                      temp.sort()
                      temp_tuple = tuple(temp)
                      if temp_tuple not in Set:
                         result.append(temp)
                         Set.add(temp_tuple)
                   hashSet.add(nums[k])

        return result
