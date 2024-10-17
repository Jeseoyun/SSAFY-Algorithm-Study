def dfs(start, visited, stack):
    current = start

    while True:
        if visited[current]:
            # 사이클이 있는지 확인
            if current in stack:
                return stack[stack.index(current):]  # 사이클 구간만 리턴
            return []

        visited[current] = True
        stack.append(current)
        current = arr[current]  # 두 번째 줄에서 다음 값으로 이동


N = int(input())
arr = [0] * (N + 1)
for i in range(1, N + 1):
    arr[i] = int(input())

result = set()
visited = [False] * (N + 1)

for i in range(1, N + 1):
    if not visited[i]:
        cycle = dfs(i, visited, [])
        result.update(cycle)  # 사이클에서 나온 값들을 결과에 추가

# 결과 출력
result = sorted(result)
print(len(result))
for num in result:
    print(num)
