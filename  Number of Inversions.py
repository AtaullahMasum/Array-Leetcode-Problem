from typing import *
def merge(a, low, mid, high, cnt ):
    temp = []
    left = low
    right = mid + 1
    while  left <= mid and right <= high:
        if a[left] <= a[right]:
            temp.append(a[left])
            left += 1
        else:
            cnt[0] += (mid - left + 1)
            temp.append(a[right])
            right += 1
    while left<= mid:
        temp.append(a[left])
        left += 1
    while right <= high:
        temp.append(a[right])
        right += 1
    for i in range(low, high+1):
        a[i] = temp[i-low]
def mergeSort(a, low, high, cnt):
    if low >= high:
        return 
    mid = (low+high)//2
    mergeSort(a, low, mid, cnt)
    mergeSort(a, mid+1, high, cnt)
    merge(a, low, mid, high, cnt)


def numberOfInversions(a : List[int], n : int) -> int:
    # Write your code here.
    cnt  = [0]
    mergeSort(a, 0, n-1, cnt)
    return cnt[0]