# grid size N 받아오기

# 각 점의 좌표 순서대로 dictionary 로 따오기

# 점의 개수대로 array 제작 (ex : [0, 1, 2, 3, 4, 5, 400]) , 0은 S, 400은 E좌표 나머지는 순서대로 
# N < 20이므로 400이상 넘어가는 코인 번호은 없다.

# ======================================================================================

# 두 점의 좌표 x1, y1, x2, y2가 주어졌을 때 두 점 사이 거리 구하는 함수 선언

# navigation array 선언. 시작점은 (0)으로 고정
# total distance array 선언 (총 이동거리에 대한 가능한 모든 경우의 수)

# choose 함수 : array가 주어졌을 때, 0번째와 -1번째를 포함한 5개의 점의 조합 구하기
    # 기저조건 : curry이 5인 경우 (출발, 도착지 포함 5개의 점을 지나고 난 후)
    # 수행할 일 : 맨뒤가 400일 경우에만 distance 계산, 구한 distance를 total distance array에 append

    # curr-1 번째까지 수를 집어넣었고, curr번째를 집어넣을 차례
    # choose(curr + 1)로 재귀

    # 시작은 choose(curr = 0)부터

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