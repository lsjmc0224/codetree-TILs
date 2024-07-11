N = int(input())
grid = [ list(map(int, input().split())) for i in range(N) ]

def get_num_of_coin(row_s, row_e, col_s, col_e):
    num_of_coin = 0
    for row in range(row_s, row_e + 1):
        for col in range(col_s, col_e + 1):
            num_of_coin += grid[row][col]

    return num_of_coin

max_coin = 0
for row in range(N):
    for col in range(N):
        if col + 2 >= N or row + 2 >= N:
            continue

        num_of_coin = get_num_of_coin(row, row + 2, col, col + 2)

        max_coin = max(num_of_coin, max_coin)

print(max_coin)