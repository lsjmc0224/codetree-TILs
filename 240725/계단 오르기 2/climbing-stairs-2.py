def max_coins(n, coins):
    # 각 층의 동전 수를 1-indexed로 맞추기 위해 앞에 0을 추가합니다.
    coins = [0] + coins
    
    # DP 테이블 초기화: dp[i][j]는 i번 위치에 도착했을 때, 정확히 j번 1계단 올랐을 때의 최대 가치
    dp = [[0 for _ in range(5)] for _ in range(n + 1)]
    
    # 기본 케이스를 초기화합니다.
    dp[1][1] = coins[1]
    if n > 1:
        dp[2][0] = coins[2]
        dp[2][2] = coins[1] + coins[2]
    
    # 동적 프로그래밍을 사용하여 최대 가치를 계산합니다.
    for i in range(3, n + 1):
        for j in range(4):
            if dp[i-2][j] != 0:
                dp[i][j] = max(dp[i][j], dp[i - 2][j] + coins[i])
            if j and dp[i - 1][j - 1] != 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + coins[i])
    
    # 가능한 모든 경우에서 최대 가치를 찾아 출력합니다.
    return max(dp[n])

# 예제 입력
n1 = int(input())
coins1 = list(map(int,input().split()))
print(max_coins(n1, coins1))