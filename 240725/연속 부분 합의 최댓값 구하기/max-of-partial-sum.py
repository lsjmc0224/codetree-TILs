import sys
INT_MIN = -sys.maxsize

n = int(input())
a = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

def init():
    for i in range(1, n+1):
        dp[i] = INT_MIN
    dp[1] = a[1]

init()

for i in range(2, n+1):
    dp[i] = max(dp[i-1] + a[i], a[i])
ans = INT_MIN

for i in range(1, n+1):
    ans = max(ans, dp[i])
print(ans)