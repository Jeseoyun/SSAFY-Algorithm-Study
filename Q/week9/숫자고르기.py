def dfs(start):                 # 2. 이때 매개변수로 받아온 start가 사이클 확인의 키가 됩니다
    stack = []
    visited = [False] * (n + 1)  # 이번 DFS 중 방문 여부 확인
    current = start             
    
    while not visited[current]:         # 방문한 곳을 또 방문했을 경우 종료합니다
        visited[current] = True         # 현재 숫자를 방문했다고 표시합니다
        stack.append(current)           # 그리고 경로 저장을 위해 stack에 추가해줍니다
        current = arr[current]          # 첫줄의 숫자 아래에 있는 값으로 넘어갑니다


    if current == start:                # 만일 종료했는데 사이클이 시작된 지점에서 종료되었을 경우
        result.extend(stack)            # result에 stack의 경로를 추가해줍니다

n = int(input())
arr = [0] * (n + 1)
for i in range(1, n + 1):
    arr[i] = int(input())

result = []

for i in range(1, n + 1): # 1. 첫번째 줄에 있는 숫자 전체 다 돌립니다
    dfs(i)

result = list(set(sorted(result)))
print(len(result))
for x in result:
    print(x)
