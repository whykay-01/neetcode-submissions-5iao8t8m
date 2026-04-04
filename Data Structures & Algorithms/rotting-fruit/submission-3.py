from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        fresh_fruit_counter = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append([row, col])
                if grid[row][col] == 1:
                    fresh_fruit_counter += 1
        
        if fresh_fruit_counter == 0:
            return 0
        
        def infect_fruit(row, col):
            nonlocal fresh_fruit_counter

            if (
                row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                grid[row][col] != 1
            ):
                return

            grid[row][col] = 2
            fresh_fruit_counter -= 1
            q.append((row, col))
        
        mins = 0

        while q and fresh_fruit_counter > 0:
            for i in range(len(q)):
                row, col = q.popleft()

                infect_fruit(row + 1, col)
                infect_fruit(row - 1, col)
                infect_fruit(row, col + 1)
                infect_fruit(row, col - 1)

            mins += 1
                
        return mins if fresh_fruit_counter == 0 else -1