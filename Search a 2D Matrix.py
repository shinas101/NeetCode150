class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row , col = len(matrix) , len(matrix[0])

        top , bot = 0 , row - 1
        while top <= bot:
            middle = (top + bot )//2
            if target > matrix[middle][-1]:
                top = middle + 1
            elif target < matrix[middle][0]:
                bot = middle - 1
            else:
                break
        
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l,r = 0 , col-1

        while l <= r:
            middle = (l + r) // 2
            if target > matrix[row][middle]:
                l = middle + 1
            elif target < matrix[row][middle]:
                r = middle - 1
            else:
                return True 
        return False
