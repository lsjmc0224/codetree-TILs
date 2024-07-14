# 그리드 벗어나는지 안벗어나는지 확인
def in_grid(x,y,n):
    return (0 <= x < n) and (0 <= y < n)

# 부딪히면 사라지는 함수
def after_collision_grid(base_grid):
    temp_base_grid = base_grid
    n = len(base_grid)
    for i in range(n):
        for j in range(n):
            if len(temp_base_grid[i][j]) > 1:
                temp_base_grid[i][j] = ''
    return temp_base_grid

# 공을 이동시키는 함수
def move_balls_grid(base_grid):
    n = len(base_grid)
    temp_move_grid = base_grid
    next_move_grid = [ [ '' for i in range(n) ] for i in range(n) ]
    global dxs, dys, dir_num_dic, num_dir_dic

    for i in range(n):
        for j in range(n):
            if len(temp_move_grid[i][j]) == 1:
                    dx = i + dxs[dir_num_dic[temp_move_grid[i][j]]]
                    dy = j + dys[dir_num_dic[temp_move_grid[i][j]]]
                    if in_grid(dx, dy, n):
                        next_move_grid[dx][dy] += temp_move_grid[i][j]
                    else:
                        init_move_num = dir_num_dic[temp_move_grid[i][j]]
                        next_move_num = (init_move_num + 2) % 4
                        next_move_dir = num_dir_dic[next_move_num]
                        next_move_grid[i][j] += next_move_dir
    return next_move_grid

# 상수 설정
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
dir_lst = ['R', 'D', 'L', 'U']
num_dir_dic = {k:v for k, v in enumerate(dir_lst)}
dir_num_dic = {v:k for k, v in enumerate(dir_lst)}
t = int(input())
for i in range(t):
    # grid 설정 입력값에 따라서 하기
    n, m = map(int, input().split())
    base_grid = [ ['' for i in range(n) ] for i in range(n) ]

    for i in range(m):
        x, y, d = map(str, input().split())
        x = int(x) - 1
        y = int(y) - 1
        base_grid[x][y] += d

    for i in range(16):
        base_grid = after_collision_grid(move_balls_grid(base_grid))

    count = 0
    for row in base_grid:
        for col in row:
            if col:
                count += 1

    print(count)