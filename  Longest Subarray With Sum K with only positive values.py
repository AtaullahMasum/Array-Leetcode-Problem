#Brute Force Solution added
"""
    Time Complexity: O( N^2 ) 
    Space Complexity: O(1)

    where N is the size of array 'A'.
"""


def longestSubarrayWithSumK(a: [int], k: int) -> int:

    n = len(a)
    # maxLength is used to store the maximum
    # length of a subarray whose sum = 'k'

    maxLength = 0

    
    for i in range(n):
        currentSum = 0
        for j in range(i, n):
            currentSum += a[j]
            if currentSum == k:
                maxLength = max(maxLength, j - i + 1)

    return maxLength
# Better Solution
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    hashMap = {}
    maxlen = 0
    Sum = 0
    for i in range(len(a)):
        Sum += a[i]
        if Sum == k:
            maxlen = max(maxlen, i+1)
        remain = Sum - k
        if remain in hashMap:
            length = i - hashMap[remain]
            maxlen = max(maxlen, length)
        if Sum not in hashMap:
            hashMap[Sum] = i
    return maxlen
# Optimal Solution Using Two Pointer and Sliding Window
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    Sum, left, right, maxlen = 0, 0, 0, 0
    
    while right < len(a):
        Sum += a[right]
        while Sum > k:
            Sum -= a[left]
            left += 1
        if Sum == k:
            maxlen = max(maxlen, right-left+1)
        right += 1
    return maxlen

