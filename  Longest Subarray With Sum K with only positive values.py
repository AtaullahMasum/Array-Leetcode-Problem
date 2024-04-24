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
