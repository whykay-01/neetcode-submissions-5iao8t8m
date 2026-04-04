class Solution:

    def exploreIsland(self, grid, row_coordinate, col_coordinate, area = 0):
        
        # out of bounds
        if row_coordinate < 0 or row_coordinate == len(grid) or col_coordinate < 0 or col_coordinate == len(grid[0]):
            return 0

        # not worth exploring
        if grid[row_coordinate][col_coordinate] == 0:
            return 0

        # the coordinate is for sure 1 - mark as visited and increment area
        grid[row_coordinate][col_coordinate] = 0

        return (1 
        + self.exploreIsland(grid, row_coordinate + 1, col_coordinate, area) 
        + self.exploreIsland(grid, row_coordinate - 1, col_coordinate, area) 
        + self.exploreIsland(grid, row_coordinate, col_coordinate + 1, area) 
        + self.exploreIsland(grid, row_coordinate, col_coordinate - 1, area)
        )



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0

        for row_coordinate in range(len(grid)):
            for col_coordinate in range(len(grid[0])):

                if grid[row_coordinate][col_coordinate] == 1:
                    
                    area = self.exploreIsland(grid, row_coordinate, col_coordinate)
                    max_area = max(max_area, area)
        
        return max_area


