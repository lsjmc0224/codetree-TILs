# n, m 격자 받아오기
n, m = map(int, input().split())
# 1 <= 각 집의 높이격자 <= 100 받아오기
house_height_arr = [ list(map(int, input().split())) for _ in range(n)]
# visited 격자 만들기 (모두 0)

# def flooded(i): flooded 격자 만들기 (잠겼으면 1 안잠겼으면 0)
    # 격자 반환
def is_flooded(k):
    for i in range(n):
        for j in range(m):
            if house_height_arr[i][j] <= k:
                flooded[i][j] = 1

# def can_go(x,y) : (visited == 0 and flooded != 0 and 격자안벗어남) 확인
def can_go(x,y):
    return  (0 <= x < n) and (0 <= y <m) and visited[x][y] == 0 and flooded[x][y] == 0
# def dfs(vertex): 안전영역탐색함수
    # dx, dy 테크닉
    # 모든 점에 대해
        # can_go면 이동
        # visited = 1
def dfs(x,y):
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
    visited[x][y] = 1
    for i in range(4):
        nxt_x = x + dxs[i]
        nxt_y = y + dys[i]
        if can_go(nxt_x, nxt_y):
            visited[nxt_x][nxt_y] = 1
            dfs(nxt_x, nxt_y)


# comfort zone array 만들기 [1]
comfort_zone_arr = [1]
k = 1

# while 1 
    # flooded = [[ 0 for _ in range(m)] for _ in range(n)]
    # flooded(k) 돌리기
    # can_go인 모든 점에 대해
        # dfs
        # 끝나면 count += 1
    # count <= comfort_zone이면 break
    # comfort zone.append(count)
    # k += 1
while 1:
    count = 0
    flooded = [[ 0 for _ in range(m)] for _ in range(n)]
    visited = [[ 0 for _ in range(m)] for _ in range(n)]
    is_flooded(k)
    for i in range(n):
        for j in range(m):
            if can_go(i,j):
                dfs(i,j)
                count += 1
    comfort_zone_arr.append(count)
    if count == 0:
        break
    k += 1

# comfort_zone 배열[-1]과 k 반환
max_comfort_zone = max(comfort_zone_arr[1:])
for i in range(1, len(comfort_zone_arr)):
    if comfort_zone_arr[i] == max_comfort_zone:
        break
print(i, max_comfort_zone)