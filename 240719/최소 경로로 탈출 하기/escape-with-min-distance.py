n, m = map(int, input().split())
visited = [ [ 0 for i in range(m)] for i in range(n)]
grid = [ list(map(int, input().split())) for i in range(n) ]
DFS_que = []
step = [ [ 0 for i in range(m)] for i in range(n)]
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
def dfs():

    while DFS_que:
        curr_v = DFS_que.pop(0)
        curr_x = curr_v[0]
        curr_y = curr_v[1]
        for i in range(4):
            nxt_x = curr_x + dxs[i]
            nxt_y = curr_y + dys[i]
            if (0 <= nxt_x < n) and (0 <= nxt_y < m) and grid[nxt_x][nxt_y] and not visited[nxt_x][nxt_y]:
                visited[nxt_x][nxt_y] = 1
                step[nxt_x][nxt_y] = step[curr_x][curr_y] + 1
                DFS_que.append((nxt_x, nxt_y))
    

DFS_que.append((0,0))
visited[0][0] = 1
dfs()
print(step[-1][-1] if step[-1][-1] else 0)