import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())
dp = [0] + [INT_MAX] * (m)
coin = [0] + list(map(int, input().split()))

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if i >= coin[j]:
            if dp[i - coin[j]] == INT_MAX:
                continue # i는 접근 불가
            
            dp[i] = min(dp[i], dp[i - coin[j]] + 1)

ans = dp[m]

if ans == INT_MAX:
    ans = -1

print(ans)