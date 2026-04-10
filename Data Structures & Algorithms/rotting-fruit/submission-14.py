from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        # init our queue with rotten fruit
        for row in range(ROWS): 
            for col in range(COLS): 
                # rotten fruit
                if grid[row][col] == 2:
                    q.append((row, col))
        
        # # no rotten fruit detected -> inval state -> return -1
        # if not q:
        #     return -1

        time_to_rotten_everything = 0

        def rotten_fruits_around(row, col):
            if row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != 1:
                return
            
            # infect
            grid[row][col] = 2
            # add newly rotten fruit to our q
            q.append((row, col))


        while q: 
            
            for _ in range(len(q)):
                r, c = q.popleft()

                rotten_fruits_around(r + 1, c)
                rotten_fruits_around(r - 1, c)
                rotten_fruits_around(r, c + 1)
                rotten_fruits_around(r, c - 1)
            
            if q:
                time_to_rotten_everything += 1
            
            

        # check for any fresh fruit left
        for row in range(ROWS): 
            for col in range(COLS): 
                # fresh fruit
                if grid[row][col] == 1:
                    # impossible state found
                    return -1

        return time_to_rotten_everything
        
        