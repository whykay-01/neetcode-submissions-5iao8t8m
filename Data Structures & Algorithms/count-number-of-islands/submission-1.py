class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def exploreIsland(row, col):
            
            if (row >= 0 and row < ROWS) and (col >= 0 and col < COLS) and (grid[row][col] == "1"):
                # mark visited
                grid[row][col] = "0"
            else:
                return
            
            exploreIsland(row + 1, col)
            exploreIsland(row - 1, col)
            exploreIsland(row, col + 1)
            exploreIsland(row, col - 1)

            
        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                # we reached an island
                if grid[row][col] == "1":
                    count += 1
                    exploreIsland(row, col)
                
        return count