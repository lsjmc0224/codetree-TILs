# grid size N 받아오기

# 각 점의 좌표 순서대로 dictionary 로 따오기

# 점의 개수대로 array 제작 (ex : [0, 1, 2, 3, 4, 5, 6]) , 0은 S, 6은 E좌표 나머지는 순서대로 

# ======================================================================================

# 두 점의 좌표 x1, y1, x2, y2가 주어졌을 때 두 점 사이 거리 구하는 함수 선언

# navigation array 선언
# answer = 0

# choose 함수 : array가 주어졌을 때, 0번째와 -1번째를 포함한 5개의 점의 조합 구하기
    # distance = 0
    # 다음 점이 정해지는대로 distance에 더하기
    # 다 정해지면, answer 과 비교하여 answer > distance면 answer = distance

n = int(input())
money_dic = {}
for i in range(n):
    temp = list(str(input()))
    for j in range(n):
        try: 
            money_dic[int(temp[j])] = [i, j]
            continue
        except:
            if temp[j] == '.':
                continue
            elif temp[j] == 'S':
                money_dic[0] = [i,j]
            else: # temp[j] == 'E'
                money_dic[400] = [i,j]
money_lst = sorted(money_dic.keys())


def dist_of_two_dots(x_arr, y_arr):
    return abs(x_arr[0] - y_arr[0]) + abs(x_arr[1] - y_arr[1])

navigation_arr = [0]
tot_dist_arr = []

def choose(curr):
    if curr == 5:
        if navigation_arr[-1] != 400:
            return
        tot_dist_int = 0
        for i in range(1, 5):
            tot_dist_int += dist_of_two_dots(money_dic[navigation_arr[i - 1]], money_dic[navigation_arr[i]])
        tot_dist_arr.append(tot_dist_int)
        return
    
    for i in money_lst[1:]:
        if navigation_arr[-1] >= i:
            continue
        navigation_arr.append(i)
        choose(curr + 1)
        navigation_arr.pop()

choose(1)
if tot_dist_arr:
    print(min(tot_dist_arr))
else:
    print(-1)