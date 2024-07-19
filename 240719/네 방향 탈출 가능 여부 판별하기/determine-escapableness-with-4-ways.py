n, m = map(int, input().split())

# grid 
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [ [0 for i in range(m)] for i in range(n)]

BFS_que = []
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def can_go(x, y):
    if not (0 <= x <n) or not (0 <= y < m):
        return False
    if grid[x][y] == 0:
        return False
    return True

def dfs():
    while BFS_que:
        curr_v = BFS_que.pop(0)
        x = curr_v[0]
        y = curr_v[1]
        for i in range(4):
            nxt_x = x + dxs[i]
            nxt_y = y + dys[i]
            if can_go(nxt_x, nxt_y) and not visited[nxt_x][nxt_y]:
                visited[nxt_x][nxt_y] = 1
                BFS_que.append((nxt_x,nxt_y))
                dfs()

BFS_que.append((0, 0))
visited[0][0] = 1
dfs()
if visited[-1][-1] == 1:
    print(1)
else:
    print(0)