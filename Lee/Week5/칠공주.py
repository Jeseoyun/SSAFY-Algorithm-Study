# https://www.acmicpc.net/problem/1941 칠공주
# 4개 갔는데 1개도 없으면 return
# 7이면 종료하고 S 4개인지 확인
# dfs 될거 같은데!?
def sol(x, y, depth, visited, temp_list):
    global result
    if depth == 4 and temp_list.count('S') == 0:  # 'S'가 4개 갔을 때 1개도 없으면 종료
        return
    if depth == 7:  # 7명이 모였을 때
        if temp_list.count('S') >= 4:  # 'S'가 4명 이상일 때만 결과 추가
            result += 1
            print(visited)
            print(temp_list)
        return

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if 0<=nx<size and 0<=ny<size and not visited[nx][ny]:
            visited[nx][ny] = True
            sol(nx, ny, depth + 1, visited, temp_list + [arr[nx][ny]])
            if temp_list:
                temp_list.pop()
            visited[nx][ny] = False


size = 5
arr = [list(input()) for _ in range(size)]

# visited = [[0] * size for _ in range(size)]
dxy = [[0,1], [0,-1], [1,0], [-1,0]]
result = 0

temp_list = []
# visited = [[False] * size for _ in range(size)]
# sol(1, 0, 1, visited, [arr[1][0]])
for i in range(size):
    for j in range(size):
        visited = [[False] * size for _ in range(size)]
        visited[i][j] = True
        sol(i, j, 1, visited, [arr[i][j]])  # 첫 번째 좌표에서 시작
        visited[i][j] = False
print(result)
