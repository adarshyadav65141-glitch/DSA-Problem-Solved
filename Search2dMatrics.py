//code-
class Solution(object):
    def searchMatrix(self, matrix, target):
        row=len(matrix)
        col=len(matrix[0])
        while row <len(matrix) and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                row+=1
            else:
                col-=1
        return False

        
