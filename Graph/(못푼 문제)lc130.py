"""
* Review
- first review 2/3/2024
- 2nd Review 3/2/2024
                                                                                                                                    
"""

from typing import List
from collections import deque

# a = "ab"

# if a == "ab":
#     print("first ")

#     # board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

#     # class Solution:
#     #     def solve(self, board: List[List[str]]) -> None:
#     #         if not board:
#     #              return None

#     #         row = len(board)
#     #         col = len(board[0])

#     #         def do_dfs(x,y):

#     #             while(deq):
#     #                 cx,cy = deq.popleft()
#     #                 directions = [(-1,0),(1,0),(0,1),(0,-1)]

#     #                 for dx,dy in directions:
#     #                     nx, ny = cx+dx + cy+dy

#     #                     if not (0<=nx<=row and 0<=ny<=col) or board[nx,ny] == "O" :
#     #                         break

#     for r in range(row):
#         for c in range(col):
#             if board[r, c] == "O":
#                 do_dfs(r, c)


board = [
    ["O", "X", "X", "O", "X"],
    ["X", "O", "O", "X", "O"],
    ["X", "O", "X", "O", "X"],
    ["O", "X", "O", "O", "O"],
    ["X", "X", "O", "X", "O"],
]


def solve(board: List[List[str]]) -> None:

    # print("solve called")
    # BFS => queue
    de = deque()

    # Search surrounded 4 region ( edge case )
    def bfs(i, j):

        while de:
            i, j = de.popleft()
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            check = True
            cnt = 0

            print("i j", i, j)
            for dx, dy in directions:
                cnt += 1
                nx, ny = i + dx, j + dy

                # print("nx ny : ", nx, ny)

                if (
                    nx == 0
                    or nx == len(board) - 1
                    or ny == 0
                    or ny == len(board[0]) - 1
                ):
                    if board[nx][ny] == "O":
                        check = False
                        break

                if board[nx][ny] == "O":
                    de.append((nx, ny))

                if cnt == 4:
                    break

            if check == True:
                board[i][j] = "X"
            print(board)

        # find 'O'

    for i in range(1, len(board) - 1):
        for j in range(1, len(board[i]) - 1):
            # print("for loop")
            if board[i][j] == "O":
                de.append((i, j))
                print(i, j)
                bfs(i, j)


# print("hh")
solve(board)
