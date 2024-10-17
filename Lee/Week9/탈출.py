# https://www.acmicpc.net/problem/3055 탈출
from collections import deque
from copy import deepcopy

# 물 BFS
def bfs_water():
    queue = deque(water_positions)
    while queue:
        x, y, time = queue.popleft()
        water_time[x][y] = time
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 범위 안이고 '.' -> 이동 가능 곳이면
            if 0 <= nx < R and 0 <= ny < C and water_grid[nx][ny] == '.':
                water_grid[nx][ny] = '*'
                queue.append((nx, ny, time + 1))


# 고슴도치 이동 BFS
def bfs_hedgehog():
    queue = deque([(hedgehog_start[0], hedgehog_start[1], 0)])
    visited[hedgehog_start[0]][hedgehog_start[1]] = True

    while queue:
        x, y, time = queue.popleft()
        # 소굴 도착
        if (x, y) == beaver_den:
            return time

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 범위 내
            if 0 <= nx < R and 0 <= ny < C:
                # 방문 안했고 이동 가능한 곳('.' or 'D')이고 물 이 지금 시간에 안차있으면
                if not visited[nx][ny] and (grid[nx][ny] == '.' or grid[nx][ny] == 'D' ) and (water_time[nx][ny] > time + 1):
                    visited[nx][ny] = True
                    queue.append((nx, ny, time + 1))ㄴ

    return -1

R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
directions = [(-1, 0), (1,0), (0,-1), (0,1)]
water_grid = deepcopy(grid) # 물 이동 시 사용
water_time = [[float('inf')] * C for _ in range(R)] # 물 이 차는 시간 저장 리스트

# 물, 고슴도치, 비버 굴 위치 저장 변수
water_positions = []
hedgehog_start = None
beaver_den = None

# S, D, * 위치 찾아서 저장
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'S':
            hedgehog_start = (r,c)
        if grid[r][c] == 'D':
            beaver_den = (r, c)
        if grid[r][c] == '*':
            water_positions.append((r,c,0))

bfs_water()

# 고슴도치의 이동 BFS
visited = [[False] * C for _ in range(R)]
result = bfs_hedgehog()

if result == -1:
    print("KAKTUS")
else:
    print(result)