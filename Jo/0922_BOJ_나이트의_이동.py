from collections import deque

#갈 수 있는 방향
dxy = [(-2,-1), (-1, -2), (1,-2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

def bfs():
    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            return visited[x][y] - 1

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < length and 0<= ny < length and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

#테스트케이스 개수
N = int(input())

for test_case in range(1, N + 1):
    # 체스판 길이
    length = int(input())
    # 2차원 visited 배열 선언
    visited = [[0] * length for _ in range(length)]
    start_x, start_y = map(int, input().split())
    visited[start_x][start_y] = 1
    end_x, end_y = map(int, input().split())
    # 초기 큐 선언
    queue = deque([(start_x, start_y)])
    result = bfs()
    print(result)

