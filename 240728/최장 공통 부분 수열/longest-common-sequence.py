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
print(longest_common_subsequence(A1, B1))