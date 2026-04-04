from collections import deque

class Solution:

    def checkAnyFreshOrangesLeft(self, grid: List[List[int]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                # fresh fruit detected
                if grid[row][col] == 1:
                    return True
        # no fresh fruit detected
        return False

    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        
        def infectOranges(row, col):
            # check for validity of the desired position
            if (
                row < 0 or
                col < 0 or
                row >= ROWS or
                col >= COLS or
                # anything but a fresh fruit
                grid[row][col] != 1
            ):
                return

            # infect the fresh fruit
            grid[row][col] = 2
            q.append([row, col])
        
        time = 0

        # initiate the queue with rotten oranges only 
        for row in range(ROWS):
            for col in range(COLS):
                # fresh fruit detected
                if grid[row][col] == 2:
                    q.append([row, col])

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()

                # explore all 4 directions
                infectOranges(row + 1, col)
                infectOranges(row - 1, col)
                infectOranges(row, col + 1)
                infectOranges(row, col - 1)
            
            if q:
                time += 1
        

        if self.checkAnyFreshOrangesLeft(grid):
            return -1
        
        return time
