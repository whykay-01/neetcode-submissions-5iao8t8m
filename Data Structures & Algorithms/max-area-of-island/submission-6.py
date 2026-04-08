class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        def exploreIsland(row, col) -> int:
            
            if (row >= 0 and row < ROWS) and (col >= 0 and col < COLS) and (grid[row][col] == 1):
                grid[row][col] = 0
                return 1 + exploreIsland(row + 1, col) + exploreIsland(row - 1, col) + exploreIsland(row, col + 1) + exploreIsland(row, col - 1)
            else:
                return 0
            
            

            
        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                # we reached an island
                if grid[row][col] == 1:
                    area = exploreIsland(row, col)
                    max_area = max(area, max_area)

        return max_area

        