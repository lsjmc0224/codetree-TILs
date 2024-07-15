n, m = map(int, input().split())

answer = []

def choose_num(curr_idx, curr_num):
    if curr_idx == m:
        for num in answer:
            print(num, end = ' ')
        print()
        return
    
    while curr_num <= n:
        if len(answer) >= 1:
            if answer[-1] >= curr_num:
                curr_num += 1
                continue
        answer.append(curr_num)
        choose_num(curr_idx + 1, 1)
        answer.pop()
        curr_num += 1
    
choose_num(0,1)