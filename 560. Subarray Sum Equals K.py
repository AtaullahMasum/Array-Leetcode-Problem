# Brute Force Solution
# Time Complexity is O(n^3)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum = 0
                for l in range(i, j+1):
                    sum += nums[l]
                if sum == k:
                    cnt += 1
        return cnt
# Better Solution 
# Time Complexity is O(n^2)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    cnt += 1
        return cnt
# Optimal Solution 
# Time Complexity is O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt , preSum = 0, 0
        hashMap = {}
        hashMap[0] = 1
        for num in nums:
            preSum  += num
            target = preSum - k
            if target in hashMap:
                 cnt += hashMap[target]
            hashMap[preSum] = hashMap.get(preSum, 0)+ 1
        return cnt
# Optimal Solution 
# Time Complexity is O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Sum , cnt = 0, 0
        hashMap ={0:1}
        for num in nums:
            Sum += num
            target = Sum - k
            if target in hashMap:
                cnt += hashMap[target]
            if Sum in hashMap:
                hashMap[Sum] += 1
            else:
                hashMap[Sum] = 1
        return cnt

          