def dfs(node, depth):
    global flag
    if depth == 5:  # 깊이가 5가 되면 조건 만족
        flag = True
        return

    # 현재 노드와 연결된 친구들 탐색
    for friend in graph[node]:
        if not visited[friend]:
            visited[friend] = True
            dfs(friend, depth + 1)
            visited[friend] = False  # 백트래킹


n, m = map(int, input().split())    # 사람 수와 친구 관계 수 입력
graph = [[] for _ in range(n)]      # 친구 관계를 저장할 그래프
visited = [False] * n               # 방문 여부를 체크할 리스트
flag = False                        # 조건을 만족하는지 여부를 확인할 플래그

# 친구 관계 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 모든 노드를 시작점으로 DFS 탐색
for i in range(n):
    visited[i] = True
    dfs(i, 1)
    visited[i] = False
    if flag:
        break

# 조건 만족 여부 출력
if flag:
    print(1)
else:
    print(0)
