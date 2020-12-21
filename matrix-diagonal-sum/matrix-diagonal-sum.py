class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagSum = 0
        size = len(mat)
        i = 0
        while i < size:
            diagSum += mat[i][i]+mat[i][size-i-1]
            i += 1
        if size%2 != 0:
            diagSum -= mat[size//2][size//2]
        return diagSum
