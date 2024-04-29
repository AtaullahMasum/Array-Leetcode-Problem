# Brute Force SOlution using four loops
# Time Complexity: O(n^4)
# Space COmplexity is : O(1)
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                for k in range(len(nums3)):
                    for l in range(len(nums4)):
                        if nums1[i] + nums2[j] + nums3[k]+nums4[l] == 0:
                            cnt += 1
        return cnt
# optimal Solution using Hashing
# Time Complexity: O(n^2+ n^2) = O(2n^2)
# Space COmplexity is : O(n^2)
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = 0
        hashDict = {}
        for num1 in nums1:
            for num2 in nums2:
                if num1+num2 in hashDict:
                    hashDict[num1+num2] += 1
                else:
                    hashDict[num1+num2]  = 1
        for num3 in nums3:
            for num4 in nums4:
                if -(num3+num4) in hashDict:
                    cnt += hashDict[-(num3+num4)]
        return cnt