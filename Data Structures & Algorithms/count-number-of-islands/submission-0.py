class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ans = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(x, y):

            visited.add((x, y))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for drow, dcol in directions:
                r, c = x + drow, y + dcol
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    ans += 1
                    dfs(i, j)


        return ans


