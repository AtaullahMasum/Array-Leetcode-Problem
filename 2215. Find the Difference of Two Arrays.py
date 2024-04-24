class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1.sort()
        nums2.sort()
        result = []
        ans = []
        hashSet = set(nums2)
        for num in nums1:
            if num not in hashSet:
                if not ans or ans[-1] != num:
                    ans.append(num)
        result.append(ans)
        hashSet1 = set(nums1)
        ans = []
        for num in nums2:
            if num not in hashSet1:
                 if not ans or ans[-1] != num:
                    ans.append(num)
        result.append(ans)
        return result
        