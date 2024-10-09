N, M = map(int, input().split())
relationship = [[] for _ in range(N)]
for _ in range(M):
  x, y = map(int, input().split())
  relationship[x].append(y)
  relationship[y].append(x)

#각 사람 방문 여부 기록
visited = [False] * N
#결과값
answer = 0

#현재 탐색 중인 사람의 인덱스(point), cnt(현재까지 탐색한 친구의 수)
def dfs(point, cnt):
  # 친구의 수가 4가 되면 조건 충족
  if cnt == 4:
    return True
  # 현재 사람의 친구 목록 순회
  for friend in relationship[point]:
    if not visited[friend]:
      visited[friend] = True
      # 재귀적으로 호출하여 친구 탐색
      if dfs(friend, cnt + 1):
        return True
      visited[friend] = False


for i in range(N):
  if not visited[i]:
    visited[i] = True
    if dfs(i, 0):
      answer = 1
      break
    visited[i] = False

print(answer)