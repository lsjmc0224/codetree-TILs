n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

def dp(grid, n):
    arr = [ [0] * n for i in range(n) ]
    arr[0][0] = grid[0][0]

    for i in range(1, n):
        arr[i][0] = arr[i-1][0] + grid[i][0]
    for j in range(1, n):
        arr[0][j] = arr[0][j-1] + grid[0][j]
    for i in range(1, n):
        for j in range(1, n):
            arr[i][j] = max(arr[i - 1][j] + grid[i][j], arr[i][j - 1] + grid[i][j])
    
    return arr[n-1][n-1]

print(dp(grid, n))