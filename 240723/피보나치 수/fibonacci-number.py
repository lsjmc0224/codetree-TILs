n = int(input())
memo = [0, 1, 1] + ([0] * (n-2))
for i in range(3, n+1):
    memo[i] = memo[i-1] + memo[i-2]

print(memo[n])