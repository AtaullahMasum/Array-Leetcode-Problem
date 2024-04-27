from typing import *

def superiorElements(a : List[int]) -> List[int]:
    ans = []
    maxi = float('-inf')
    for i in range(len(a)-1, -1, -1):
        if a[i] > maxi:
            ans.append(a[i])
            maxi = a[i]
    ans.sort()
    return ans
