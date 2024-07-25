'''
1. D(i, j) : 1번째 ~ i번째 원소까지 참조했을때, 부분수열의 합이 j인 부분수열의 최소 길이
2. 초기화
    D(0, 0) = 0
    D(0, j) = 무한대 (불가능) 
3. 점화식
    D(i, j)
        1. i번째 원소를 더해서 j 가 된 경우 D(i, j-arr[i]) + 1
        2. i번재 원소를 더하지 않아도 j가 된 경우 D(i-1, j)
        3. 둘중 최소가 D(i,j)
'''

# import sys
# MAXNUM = sys.maxsize
# arr = [5,2,4,1,6]
# n, m = 5, 12
# output_grid = [ [0] * (m+1) for i in range(n) ]

# def init():
#     for i in range(n):
#         for j in range(m+1):
#             output_grid[i][j] = MAXNUM
#     output_grid[0][arr[0]] = 1
# for i in range(1, n):
#     for j in range(m+1):
#         if j < arr[i]:
#             continue
#         output_grid[i][j] = min(output_grid[i][j-arr[i]] + 1, output_grid[i-1][j])
# init()
# print(output_grid)

N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))

# N + 1 * M + 1
D = [
    [ -1 for _ in range(M+1)]
    for _ in range(N+1)
]

D[0][0] = 0
for i in range(1, N+1):
    for j in range(0, M + 1):
        res = -1
        if j-A[i] >= 0 and D[i-1][j-A[i]] != -1:
            res = D[i-1][j-A[i]] +1
        if D[i-1][j] != -1 and (res == -1 or D[i-1][j] < res):
            res = D[i-1][j]
        D[i][j] = res

# 1 ~ N동전 써서 N원을 만드는경우

print(D[N][M])