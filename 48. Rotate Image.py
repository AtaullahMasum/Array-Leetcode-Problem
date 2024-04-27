# Optimal Solution 
# Time Complexity is O(n/2*n/2) + O(n*n/2)
# Space Complexity is O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            for j in range(n//2):
                matrix[i][j] , matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]