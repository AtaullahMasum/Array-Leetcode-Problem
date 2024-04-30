# Optimal SOlution using HashMap
# Time COmpelxity is : O(n)
# Space Complexity is : O(n)
def subarraysWithSumK(a: [int], b: int) -> int:
    # Write your code here
    hashDict = {0: 1}
    XOR = 0
    cnt = 0
    for num in a:
        XOR = XOR ^ num
        target = XOR ^ b
        if target in hashDict:
            cnt += hashDict[target]
        if XOR in hashDict:
            hashDict[XOR] += 1
        else:
            hashDict[XOR] = 1
    return cnt
