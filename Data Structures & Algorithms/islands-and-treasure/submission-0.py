"""
[
  [G,-1,0,G],
  [G,G,G,-1],
  [G,-1,G,-1],
  [0,-1,G,G]
]
G = 2147483647
replace each G with min(distances_to_chests)

keep exploring the graph via G until 0 is seen 
but be mindful of:
    
    .) -1 (water is not traversible)

"""
from collections import deque

class Solution:

    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        dist = 0

        # let's init the queue with our treasuries first
        for row in range(ROWS):
            for col in range(COLS): 
                if grid[row][col] == 0:
                    visited.add((row, col))
                    q.append([row, col])


        def add_land(row, col):

            if row < 0 or row == ROWS or col < 0 or col == COLS or (row, col) in visited or grid[row][col] == -1:
                return

            visited.add((row, col))
            q.append([row, col])

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                # explore in 4 directions
                add_land(r + 1, c)
                add_land(r - 1, c)
                add_land(r, c + 1)
                add_land(r, c - 1)

            dist += 1


