n = int(input())
arr = [0] + list(map(int, input().split()))
sorted_arr = sorted(arr)


for i in range(1, n+1):
    target = arr[i]
    for j in range(1, n+1):
        if sorted_arr[j] == target:
            print(j, end = ' ')
            sorted_arr[j] = -1
            break