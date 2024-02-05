# first review 2/3/2024

from typing import List
from collections import deque

a = "ab"
if a =="ab":
        print ("first ")

# board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         if not board:
#              return None
        
#         row = len(board)
#         col = len(board[0])

#         def do_dfs(x,y):
           

#             while(deq):
#                 cx,cy = deq.popleft()
#                 directions = [(-1,0),(1,0),(0,1),(0,-1)]

#                 for dx,dy in directions:
#                     nx, ny = cx+dx + cy+dy

#                     if not (0<=nx<=row and 0<=ny<=col) or board[nx,ny] == "O" :
#                         break



        
        

        for r in range(row):
            for c in range(col):
                if(board[r,c]=='O'):
                    do_dfs(r,c)

        


        