def edit_distance(A, B):
    N = len(A)
    M = len(B)
    
    # DP 테이블 초기화
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # 기본 경우 초기화
    for i in range(1, N + 1):
        dp[i][0] = i
    for j in range(1, M + 1):
        dp[0][j] = j
        
    # DP 점화식 채우기
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
                
    return dp[N][M]

# 입력 받기
A = input().strip()
B = input().strip()

# 편집 거리 계산 및 출력
print(edit_distance(A, B))