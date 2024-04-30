# Optimal Solution 1
# Time Complexity is : O(min(n,m)) + O(nlogn) + O(mlogm)
# Space Complexity is : O(1)
from typing import *

def mergeTwoSortedArraysWithoutExtraSpace(a : List[int], b : List[int]) -> int:
    # Write your code here.
    left = len(a)-1
    right = 0
    while left >= 0 and right < len(b):
        if a[left] > b[right]:
            a[left], b[right] = b[right], a[left]
            left -= 1
            right += 1
        else:
            break
    a.sort()
    b.sort()
# Optimal Solution 2
# Time Complexity is : O(log(m+n)*(m+n))
# Space Complexity is : O(1)
from typing import *
def swapIfgreater(a, b, index1, index2):
    if a[index1] > b[index2]:
        a[index1], b[index2] = b[index2], a[index1]

def mergeTwoSortedArraysWithoutExtraSpace(a : List[int], b : List[int]) -> int:
    # Write your code here.
    n, m = len(a), len(b)
    Len =(n+m)
    gap = (n+m)//2 +(n+m)%2
    while gap > 0:
        left = 0
        right = left + gap
        while right < Len:
            # arr1 and arr2
            if left < n and right >= n:
                swapIfgreater(a, b, left, right-n)
            # arr2 and arr2
            elif left >= n:
                swapIfgreater(b, b, left-n, right-n)
            # arr1 and arr1
            else:
                swapIfgreater(a, a, left, right)
            left += 1
            right += 1
        if gap == 1:
            break
        gap = (gap)//2 + gap%2