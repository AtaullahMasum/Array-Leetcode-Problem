from sys import *
from collections import *
from math import *

def getLongestSubarray(nums: [int], k: int) -> int:
    # Write your code here
    hashMap = {}
    maxlen = 0
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum == k:
            maxlen = max(maxlen, i+1)
        remain = sum - k
        if remain in hashMap:
            length = i - hashMap[remain]
            maxlen = max(maxlen, length)
        if sum not in hashMap:
            hashMap[sum] = i
    return maxlen
