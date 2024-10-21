from collections import deque

# 방향 벡터 설정
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 입력 받기
r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

# 방문 배열 초기화
visit_water = [[-1] * c for _ in range(r)]
visit_ramge = [[-1] * c for _ in range(r)]
w_q = deque()  # 물의 BFS를 위한 큐
ramge_q = deque()  # 고슴도치의 BFS를 위한 큐
exit_x, exit_y = -1, -1  # 비버 굴 위치

# 초기 상태 설정
for i in range(r):
    for j in range(c):
        if arr[i][j] == '*':  # 물이 있는 곳
            w_q.append((i, j))
            visit_water[i][j] = 0  # 물의 초기 위치
        elif arr[i][j] == 'S':  # 고슴도치 시작 위치
            ramge_q.append((i, j))
            visit_ramge[i][j] = 0
        elif arr[i][j] == 'D':  # 비버의 굴 위치
            exit_x, exit_y = i, j

# 물 BFS
while w_q:
    cur_x, cur_y = w_q.popleft()
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and visit_water[nx][ny] == -1:
            if arr[nx][ny] == '.':  # 빈 공간으로만 물이 확장됨
                w_q.append((nx, ny))
                visit_water[nx][ny] = visit_water[cur_x][cur_y] + 1

# 고슴도치 BFS
while ramge_q:
    cur_x, cur_y = ramge_q.popleft()
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and visit_ramge[nx][ny] == -1:
            if arr[nx][ny] == 'D':  # 비버의 굴에 도착한 경우
                print(visit_ramge[cur_x][cur_y] + 1)
                exit()
            if arr[nx][ny] == '.' and (visit_water[nx][ny] == -1 or visit_ramge[cur_x][cur_y] + 1 < visit_water[nx][ny]):
                ramge_q.append((nx, ny))
                visit_ramge[nx][ny] = visit_ramge[cur_x][cur_y] + 1

# 비버 굴에 도달하지 못한 경우
print('KAKTUS')
