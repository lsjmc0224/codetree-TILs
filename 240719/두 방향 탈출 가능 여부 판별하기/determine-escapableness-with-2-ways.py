n, m = map(int, input().split())

# grid 받아오기 
grid = [ list(map(int, input().split())) for i in range(n) ]
visited = [ [0 for i in range(m)] for i in range(n) ]
def can_go(x,y):
    if not ( 0 <= x < n ) or not ( 0 <= y < m ):
        return False
    
    if grid[x][y] == 0:
        return False
    
    return True

def dfs(curr_x, curr_y):
    dxs = [1, 0]
    dys = [0, 1]
    visited[curr_x][curr_y] = 1

    for i in range(2):
        nxt_x = curr_x + dxs[i]
        nxt_y = curr_y + dys[i]

        if can_go(nxt_x, nxt_y) and not visited[nxt_x][nxt_y]:
            dfs(nxt_x, nxt_y)

dfs(0,0)

if visited[-1][-1] == 1:
    print(1)
else:
    print(0)