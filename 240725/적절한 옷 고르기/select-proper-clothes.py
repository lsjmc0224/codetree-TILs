def max_satisfaction(N, M, clothes):
    # DP 배열 초기화
    dp = [[-1] * (N + 1) for _ in range(M + 1)]
    
    # 각 옷의 화려함을 저장할 배열
    glamor = [0] * (N + 1)
    
    # 각 옷의 입을 수 있는 시작 날짜와 끝 날짜를 저장할 배열
    start = [0] * (N + 1)
    end = [0] * (N + 1)
    
    # 옷 정보 입력
    for i in range(N):
        s, e, v = clothes[i]
        start[i + 1] = s
        end[i + 1] = e
        glamor[i + 1] = v
    
    # 첫 날 초기화
    for i in range(1, N + 1):
        if start[i] == 1:
            dp[1][i] = 0
    
    # DP 테이블 채우기
    for day in range(2, M + 1):
        for current in range(1, N + 1):
            if start[current] <= day <= end[current]:
                for previous in range(1, N + 1):
                    if dp[day - 1][previous] != -1 and start[previous] <= day - 1 <= end[previous]:
                        current_glam = abs(glamor[current] - glamor[previous])
                        dp[day][current] = max(dp[day][current], dp[day - 1][previous] + current_glam)
    
    # 최대 만족도 찾기
    max_satisfaction = 0
    for i in range(1, N + 1):
        if dp[M][i] != -1:
            max_satisfaction = max(max_satisfaction, dp[M][i])
    
    return max_satisfaction

N1, M1 = map(int, input().split())
clothes1 = [list(map(int, input().split())) for i in range(N1)]
print(max_satisfaction(N1, M1, clothes1))