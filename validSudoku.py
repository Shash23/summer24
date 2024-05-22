from typing import List

class Solution:
    
    def findDuplicates(self, row: List[int]) -> bool:
        
        freqs = {}

        for num in row:
            
            if(num == '.'):
                continue
    
            # avoids key error
            
            if (freqs.get(num, 0) == 1):
                # print(num)
                # print("yay")
                # exit(0)
                
                return False
            
            else:
                freqs[num] = freqs.get(num, 0) + 1
                
        return True
    
    def checkUnique(self, square: List[List[str]]) -> bool:
        
        for row in range(0,9,3):
            
            for col in range(0,9,3):
                
                grid = [
                    
                    board[row+i][col + j]
                    for i in range(0, 3)
                    for j in range(0, 3)
                    
                ]
                
                if (not findDuplicates(grid)):
                    return False
                
        return True
        
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check each row and column to see if there any duplicates in the row, if so, then 

        for row in board:
            
            if(not self.findDuplicates(row)):
                
                return False
            
        cols = list(zip(*board))
        
        for col in cols:
            
            if(not self.findDuplicates(col)):
                
                return False
            
        # now check each 3 x 3
        if( not self.checkUnique(board) ):
            
            return False
        
        