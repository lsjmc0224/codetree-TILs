N, M = map(int, input().split())
field_arr = [ [0 for i in range(N)] for j in range(N) ]

drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]

for i in range(M):
    output_cnt = 0
    r, c = map(int, input().split())
    r = r - 1
    c = c - 1
    field_arr[r][c] = 1
    cnt = 0
    for dir_num in range(4):
        nr, nc = r + drs[dir_num], c + dcs[dir_num]
        if (0 <= nr < N) and (0 <= nc < N) and field_arr[nr][nc]:
            cnt += 1
    if cnt == 3:
        output_cnt = 1

    print(output_cnt)