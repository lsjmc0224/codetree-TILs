def max_coins(n, coins):
    # dp[i][j]는 i번째 계단에 도달했을 때, 1계단 오르기를 j번 사용한 경우의 최대 동전 수
    dp = [[-float('inf')] * 4 for _ in range(n)]

    # 초기 조건 설정
    dp[0][0] = coins[0]
    if n > 1:
        dp[1][1] = coins[1]

    for i in range(2, n):
        for j in range(4):
            if j < 3 and dp[i-1][j] != -float('inf'):  # 1계단 오르기
                dp[i][j+1] = max(dp[i][j+1], dp[i-1][j] + coins[i])
            if dp[i-2][j] != -float('inf'):  # 2계단 오르기
                dp[i][j] = max(dp[i][j], dp[i-2][j] + coins[i])

    # n-1층에서 얻을 수 있는 최대 동전 수 찾기
    return max(dp[n-1])

# 예제 입력
n1 = int(input())
coins1 = list(map(int,input().split()))
print(max_coins(n1, coins1))