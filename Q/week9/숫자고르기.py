n = int(input())
arr = [0] * (n + 1)
for i in range(1, n + 1):
    arr[i] = int(input())

result = []


def dfs(start):
    stack = []
    visited = [False] * (n + 1)  # 이번 DFS 중 방문 여부 확인
    current = start

    while not visited[current]:
        visited[current] = True
        stack.append(current)
        current = arr[current]

    if current == start:
        result.extend(stack)  # 사이클을 발견한 경우


for i in range(1, n + 1):
    dfs(i)

result = list(set(sorted(result)))
print(len(result))
for x in result:
    print(x)
