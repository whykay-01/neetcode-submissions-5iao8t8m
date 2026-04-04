class Solution:
    
    def exploreIsland(self, grid, row_coordinate: int, col_coordinate: int):
        
        if row_coordinate < 0 or row_coordinate == len(grid) or col_coordinate < 0 or col_coordinate == len(grid[0]):
            return
        
        # we have already explored this node and counted it
        if grid[row_coordinate][col_coordinate] == "0":
            return 
        
        # mark visited by -1
        grid[row_coordinate][col_coordinate] = "0"

        # explore all directions
        self.exploreIsland(grid, row_coordinate - 1, col_coordinate)
        self.exploreIsland(grid, row_coordinate + 1, col_coordinate)
        self.exploreIsland(grid, row_coordinate, col_coordinate - 1)
        self.exploreIsland(grid, row_coordinate, col_coordinate + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        for row_coordinate in range(len(grid)):
            for col_coordinate in range(len(grid[0])):
                
                # start the DFS
                if grid[row_coordinate][col_coordinate] == "1":
                    self.exploreIsland(grid, row_coordinate, col_coordinate)
                    counter += 1
                
        return counter
