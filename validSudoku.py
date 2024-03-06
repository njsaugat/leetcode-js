import collections
class Solution:
    def isValidSudoku(self,board):
        cols=collections.defaultdict(set)
        rows=collections.defaultdict(set)
        squares=collections.defaultdict(set) # key = (r//3, c//2)
        # inside a dict we are adding a set
        # like the value can only be set
        # got it got it
        # every shape tha we need has a set
        # we need to validate the rows
        # so rows has a set
        # like 0 is the key and the values that will be added there
        # 
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[r//3,c//3]
                ):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True
    
    
    def isSudoku(self, board):
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        squares=collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                
                if board[r][c]==".":
                    continue
                
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in board[r//3,c//3] 
                ):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r//3,c//3].add(board[r][c])
        return True
    
    