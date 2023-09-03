# 첫번째 풀이
from collections import deque

class Solution:
    def bfs(self, node, n, m, visited, grid):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        q = deque([node])

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[ny][nx] and grid[ny][nx] == '1':
                        q.append([nx, ny])
                        visited[ny][nx] = True

    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        col, row = len(grid), len(grid[0])a
        visited = [[False] * row for _ in range(col)]

        for y in range(col):
            for x in range(row):
                if grid[y][x] == '1' and visited[y][x] == False:
                    self.bfs([x, y], row, col, visited, grid)
                    answer += 1
        return answer


# 두번째 풀이

from collections import deque

class Solution:
    def bfs(self, node, n, m, grid):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        q = deque([node])

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if grid[ny][nx] == '1':
                        q.append([nx, ny])
                        grid[ny][nx] = "0"

    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        col, row = len(grid), len(grid[0])
        
        for y in range(col):
            for x in range(row):
                if grid[y][x] == '1':
                    self.bfs([x, y], row, col, grid)
                    answer += 1
        return answer