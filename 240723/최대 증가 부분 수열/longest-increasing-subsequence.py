import sys
MIN_NUM = -sys.maxsize

n = 4
inp_arr = [0] + [1, 3, 2, 4]

dp = [1] * (n + 1)  # 각 원소는 적어도 자기 자신 하나로 부분 수열을 구성할 수 있으므로 1로 초기화

for i in range(2, n + 1):
    for j in range(1, i):
        if inp_arr[j] < inp_arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

ans = 0
for i in range(1, n + 1):
    ans = max(ans, dp[i])

print(ans)