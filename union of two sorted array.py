# Using Two pointer Approch
# Time Complexity is O(n1+n2)
# Space Complexity is O(1) but result has O(n1 + n2)
class Solution:
    def unionTwoSortedArray(self, nums1, nums2):
        union = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                if len(union) == 0 or union[-1] != nums1[i]:
                    union.append(nums1[i])
                    i += 1
            else:
                if len(union) == 0 or union[-1] != nums2[j]:
                    union.append(nums2[j])
                    j += 1
        while i < len(nums1):
            if len(union) == 0 or union[-1] != nums1[i]:
                union.append(nums1[i])
                i += 1
        while j < len(nums2):
            if len(union) == 0 or union[-1] != nums2[j]:
                union.append(nums2[j])
                j += 1
        return union
        