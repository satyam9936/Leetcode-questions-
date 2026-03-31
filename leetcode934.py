#leetcode 934. Shortest Bridge
from ast import List        
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = []

        def dfs(r, c):
            visited[r][c] = True
            queue.append((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and not visited[nr][nc]:
                    dfs(nr, nc)

        found = False
        for i in range(rows):
            if found:
                break
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        steps = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.pop(0)
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                        if grid[nr][nc] == 1:
                            return steps
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            steps += 1

        return -1