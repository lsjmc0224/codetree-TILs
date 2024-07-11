n, t= tuple(map(int, input().split()))
u = list(map(int, input().split()))
d = list(map(int, input().split()))
for _ in range(t):
    temp = u[n-1]
    for i in range(n-1, 0, -1):
        u[i] = u[i - 1]
    u[0] = d[n - 1]

    for i in range(n-1, 0 ,-1):
        d[i] = d[i-1]
    d[0] = temp

for i in range(n):
    print(u[i], end= ' ')
print()
for i in range(n):
    print(d[i], end= ' ')