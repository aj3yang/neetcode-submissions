class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        n = len(heights)
        m = len(heights[0])

        def dfs(x, y, visited, prevHeight):
            if ((x, y) in visited or x < 0 or y < 0 or x == n or y == m or heights[x][y] < prevHeight):
                return
            visited.add((x, y))
            dfs(x + 1, y, visited, heights[x][y])
            dfs(x - 1, y, visited, heights[x][y])
            dfs(x, y + 1, visited, heights[x][y])
            dfs(x, y - 1, visited, heights[x][y])

        for i in range(m):
            dfs(0 , i, pacific, heights[0][i])
            dfs(n-1, i, atlantic, heights[n-1][i])

        for i in range(n):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, m-1, atlantic, heights[i][m-1])

        ans = []
        for i in range(n):
            for j in range(m):
                if (i, j) in pacific and (i, j) in atlantic:
                    ans.append([i, j])

        return ans

        