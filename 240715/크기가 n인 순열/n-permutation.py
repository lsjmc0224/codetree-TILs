n = int(input())
visited = [0] * (n+1)
answer = []

def choose_num(curr_idx):
    if curr_idx == n + 1:
        for num in answer:
            print(num, end = ' ')
        print()
        return
    
    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = 1
        answer.append(i)
        choose_num(curr_idx + 1)
        answer.pop()
        visited[i] = 0

choose_num(1)