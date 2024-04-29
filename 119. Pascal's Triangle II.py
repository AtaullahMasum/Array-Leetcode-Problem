# Optimal Solution added
# Time Complexity is O(n)
class Solution:
    def nthrow(self, row):
        result = []
        ans = 1
        result.append(ans)
        for i in range(1,row):
            ans = ans*(row - i)
            ans = ans//i
            result.append(ans)
        return result
    def getRow(self, rowIndex: int) -> List[int]:
        return self.nthrow(rowIndex+1)
       