def longest_common_subsequence(A, B):
    N = len(A)
    M = len(B)

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[N][M]

A1 = input()
B1 = input()

# 편집거리 구하기: A1에서 최장 공통 부분 수열 길이를 뺀만큼 삭제하고, B1에서 최장 공통 부분 수열 길이를 뺀만큼 추가해한다.
# 따라서 편집거리 = len(A1) - longest_common_subsequence(A1, B1) + len(B1) - longest_common_subsequence(A1, B1)

print(len(A1) + len(B1) - 2 * longest_common_subsequence(A1, B1))