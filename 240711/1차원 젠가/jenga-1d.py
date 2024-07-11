n = int(input())
jenga = [ int(input()) for i in range(n) ]

for t in range(2):
    start, end = map(int, input().split())
    start = start - 1
    end = end - 1
    temp = []
    for i in range(len(jenga)):
        if start <= i <= end:
            continue
        temp.append(jenga[i])
    jenga = temp
print(len(jenga))
for num in jenga:
    print(num)