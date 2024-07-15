k, n = map(int, input().split())
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=' ')
    print()

def choose(curr_idx, curr_num):
    global k, n
    if curr_idx == n:
        print_answer()
        return 
    while curr_num <= k:
        answer.append(curr_num)
        choose(curr_idx + 1, 1)
        answer.pop()
        curr_num += 1
    return

choose(0, 1)