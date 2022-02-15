class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        l = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
 
                if matrix[i][j] == 0:
                    l.append([i,j])
        

        for i in l:
            for b in range(len(matrix[0])):
                matrix[i[0]][b] = 0
            for a in range(len(matrix)):
                matrix[a][i[1]] = 0
                