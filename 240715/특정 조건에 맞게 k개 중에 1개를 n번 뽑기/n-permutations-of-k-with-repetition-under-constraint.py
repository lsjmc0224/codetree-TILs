k, n = map(int, input().split())

answer = []

def print_answer():
    for ans in answer:
        print(ans, end = ' ')
    return

def choose(curr_idx, curr_num):
    global k, n
    if curr_idx == n:
        print_answer()
        print()
        return

    while curr_num <= k:
        if len(answer) >= 2:
            if (answer[curr_idx-1] == answer[curr_idx-2] == curr_num):
                curr_num += 1
                continue
        answer.append(curr_num)
        choose(curr_idx + 1, 1)
        answer.pop()
        curr_num += 1
    return

choose(0, 1)