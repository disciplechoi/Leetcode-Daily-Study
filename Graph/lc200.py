"""
* Review
- 1st review : 1/31/2024
- 2nd review : 2/21/2024



* Solution
1) 
from typing import List

grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

#print("leg(grid) :", len(grid))

class Solution:
     def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(i,j) :
            queue = []
            queue.append((i,j))

            while queue:  
                current_i, current_j = queue.pop(0)
                grid[current_i][current_j] = "0"
                print("current_i, current_j :", current_i,", ",current_j)

                
                if current_j == len(grid[current_i])-1 and current_i+1<len(grid)-1:
                    if grid[current_i+1][current_j] == "1" :
                        queue.append((current_i+1,current_j))
                    
                elif current_i == len(grid)-1 and current_j+1<len(grid[current_i])-1:
                    if grid[current_i][current_j+1] == "1":
                        queue.append((current_i,current_j+1))
 
                if current_i+1 < len(grid):
                    if grid[current_i+1][current_j]=="1" :
                                queue.append((current_i+1,current_j))

                if current_j+1 < len(grid[current_i]):
                    if grid[current_i][current_j+1]=="1":
                                queue.append((current_i,current_j+1))



        number = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    number+=1
                    

                    if i != (len(grid)-1) or j != (len(grid[i])-1):
                        # print("bfs is called")
                        bfs(i,j)
        
        return number
     

sol = Solution()
print("answer : ",sol.numIslands(grid))
print(grid)
            
"""

TC(M * N)
SC(M * N)
import collections
from typing import List

grid = [["1"], ["1"]]

number = 0
de = collections.deque()


def numIslands(grid: List[List[str]]) -> int:
    number = 0
    de = collections.deque()

    def dfs():

        while de:
            i, j = de.popleft()
            print(i, j)

            if i + 1 < len(grid) and grid[i + 1][j] == "1":
                de.append((i + 1, j))
                grid[i + 1][j] = "0"
            if i - 1 >= 0 and grid[i - 1][j] == "1":
                de.append((i - 1, j))
                grid[i - 1][j] = "0"

            if j - 1 >= 0 and grid[i][j - 1] == "1":
                de.append((i, j - 1))
                grid[i][j - 1] = "0"

            if j + 1 < len(grid[0]) and grid[i][j + 1] == "1":
                de.append((i, j + 1))
                grid[i][j + 1] = "0"

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == "1":
                number += 1
                print("here")
                de.append((i, j))
                dfs()

    return number


print(numIslands(grid))
