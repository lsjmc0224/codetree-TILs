from itertools import combinations
from collections import deque

def bfs(grid, start, end, n):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True
    distance = [[-1] * n for _ in range(n)]
    distance[start[0]][start[1]] = 0

    while queue:
        r, c = queue.popleft()
        if (r, c) == end:
            return distance[r][c]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                visited[nr][nc] = True
                distance[nr][nc] = distance[r][c] + 1
                queue.append((nr, nc))
    return -1

def min_time_to_reach(n, k, grid, start, end):
    walls = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
    min_time = float('inf')
    found = False
    
    for walls_to_remove in combinations(walls, k):
        new_grid = [row[:] for row in grid]
        for r, c in walls_to_remove:
            new_grid[r][c] = 0
        time = bfs(new_grid, start, end, n)
        if time != -1:
            found = True
            min_time = min(min_time, time)
    
    return min_time if found else -1

# 입력 예제
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
x, y = map(int, input().split())
start = (x-1, y-1)
x, y = map(int, input().split())
end = (x-1, y-1)

print(min_time_to_reach(n, k, grid, start, end))