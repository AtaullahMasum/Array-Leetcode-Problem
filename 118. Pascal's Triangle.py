class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        for i in range(numRows):
            dp1 = []
            for j in range(i+1):
                if j == 0 or j==i:
                    dp1.append(1)
                else:
                    dp1.append(dp[i-1][j-1]+dp[i-1][j])          
            dp.append(dp1)
        return dp