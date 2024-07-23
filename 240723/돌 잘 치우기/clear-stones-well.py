from itertools import combinations
from collections import deque

def max_reachable_cells(n, k, m, grid, starts):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 돌의 위치 찾기
    rocks = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
    
    def bfs(grid, starts):
        visited = [[False] * n for _ in range(n)]
        queue = deque(starts)
        count = 0
        
        for r, c in starts:
            visited[r][c] = True
            
        while queue:
            r, c = queue.popleft()
            count += 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        
        return count

    max_cells = 0
    
    # 돌의 조합을 선택하여 제거
    for rocks_to_remove in combinations(rocks, m):
        new_grid = [row[:] for row in grid]
        for r, c in rocks_to_remove:
            new_grid[r][c] = 0
        
        max_cells = max(max_cells, bfs(new_grid, starts))
    
    return max_cells

n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
starts = []
for i in range(k):
    x, y = map(int, input().split())
    starts.append((x-1, y-1))

print(max_reachable_cells(n, k, m, grid, starts))