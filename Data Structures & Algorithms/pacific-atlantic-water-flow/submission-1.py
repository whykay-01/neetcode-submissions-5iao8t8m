class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(row, col, visit, prev_height):
            if (
                ((row, col) in visit) or
                (row < 0 or col < 0 or row == ROWS or col == COLS) or
                heights[row][col] < prev_height
            ):
                return 
            
            visit.add((row, col))
            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])

        for c in range(COLS):
            # pass the 0th and last rows
            dfs(
                row=0, 
                col=c, 
                visit=pacific, 
                prev_height=heights[0][c])
            dfs(
                row=ROWS-1, 
                col=c, 
                visit=atlantic, 
                prev_height=heights[ROWS-1][c])

        for r in range(ROWS):
            # pass the 0th and last cols
            dfs(
                row=r,
                col=0,
                visit=pacific,
                prev_height=heights[r][0])
            dfs(
                row=r,
                col=COLS-1,
                visit=atlantic,
                prev_height=heights[r][COLS-1])
        
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        
        return result