from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        dist = 0

        # bfs and init the q with the chests
        for row in range(ROWS):
            for col in range(COLS):
                # chest is found
                if grid[row][col] == 0:
                    visited.add((row, col))
                    q.append((row, col))
        
        
        def add_land(row, col):
            if row < 0 or row == ROWS or col < 0 or col == COLS or (row, col) in visited or grid[row][col] == -1:
                return 
            
            visited.add((row, col))
            q.append((row, col))
        
        while q:
            
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                # explore 4 dir
                add_land(r + 1, c)
                add_land(r - 1, c)
                add_land(r, c + 1)
                add_land(r, c - 1)
            
            dist += 1


