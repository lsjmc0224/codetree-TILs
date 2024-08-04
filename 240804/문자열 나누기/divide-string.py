n = int(input())
arr = ''.join(list(map(str, input().split())))
i = 0
while 1:
    if i == len(arr):
        break
    print(arr[i], end = '')
    if (i + 1) % 5 == 0:
        print()
    i += 1