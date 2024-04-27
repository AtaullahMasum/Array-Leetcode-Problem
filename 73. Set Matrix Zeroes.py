# Better SOlution 
# Time Complexity is O(2n*m)
# Space Complexity is O(n+m)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        row = [0]*n
        col = [0]*m
        for i in range(n):
           for j in range(m):
              if matrix[i][j] == 0:
                 row[i] = 1
                 col[j] = 1
        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        
# Optimal Solution 
# Time Complexity is O(2*n*m) + O(n)+O(m)
# Space Complexity is O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n , m = len(matrix), len(matrix[0])
        col0 = 1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        for i in range(1, n):
            for j in range(1, m):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if not matrix[0][0]:
            for j in range(m):
                matrix[0][j] = 0
        if not col0:
            for i in range(n):
                matrix[i][0] = 0

        