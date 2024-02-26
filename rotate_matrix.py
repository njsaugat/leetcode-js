class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):

                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp

        
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
        
        return matrix

print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))