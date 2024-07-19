# 인접 리스트 작성
n, m = map(int, input().split())
graph = [ [] for i in range(n+1) ]

for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [0] * (n + 1)
count = 0
# dfs 함수 작성 (1번에서 갈수있는 정점의 수)
def dfs(vertex):
    global count
    for nxt in graph[vertex]:
        if visited[nxt]:
            continue
        visited[nxt] = 1
        count += 1
        dfs(nxt)

INITIAL_VERTEX = 1
visited[INITIAL_VERTEX] = 1
dfs(INITIAL_VERTEX)
print(count)