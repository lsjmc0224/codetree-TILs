n, m, t = map(int, input().split())
grid = [ list(map(int, input().split())) for _ in range(n) ]
count = [ [ 0 for i in range(n) ] for i in range(n) ]
for i in range(m):
    x, y = map(int, input().split())
    x = x-1
    y = y-1
    count[x][y] += 1

def valid_cell(x, y):
    global n
    return (0 <= x < n) and (0 <= y < n)

def move_marble(x, y):
    global grid
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    max_num = 0
    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if valid_cell(nx, ny) and grid[nx][ny] > max_num:
            ox = nx
            oy = nx
    return ox, oy
    
for i in range(t):
    new_count = [ [ 0 for i in range(n) ] for i in range(n) ]
    for i in range(n):
        for j in range(n):
            if count[i][j] == 0:
                continue
            x, y = move_marble(i, j)
            new_count[x][y] += 1
    for i in range(n):
        for j in range(n):
            if new_count[i][j] >= 0:
                new_count[i][j] == 0

    count = new_count

marble_count = 0
for i in range(n):
    for j in range(n):
        marble_count += count[i][j]
print(marble_count)