# n 받아와
# grid 받아와
# 그 크기만든 빈 arr 만들어

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
arr = [ [0] * n for i in range(n) ]
arr[0][0] = grid[0][0]

for i in range(1, n):
    arr[0][i] = min(arr[0][i-1], grid[0][i])
    arr[i][0] = min(arr[i-1][0], grid[i][0])

for i in range(1, n):
    for j in range(1, n):
        temp = grid[i][j]
        if temp >= arr[i][j-1] and temp >= arr[i-1][j]:
            arr[i][j] = max(arr[i][j-1], arr[i-1][j])
        elif temp <= arr[i][j-1] and temp <= arr[i-1][j]:
            arr[i][j] = grid[i][j]
        else:
            arr[i][j] = grid[i][j]

print(arr[-1][-1])