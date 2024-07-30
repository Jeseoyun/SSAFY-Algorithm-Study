from collections import deque

# import sys
# sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    num = int(input())
    # 16 X 16 미로
    maze = [list(map(int, list(input()))) for _ in range(16)]
    # 출발점 설정
    start_point = (1,1)
    # 큐에 삽입
    queue = deque([start_point])

    # 4방향 이동. 우 상 좌 하
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    # 재방문 방지를 위한 visited 테이블
    visited = [[False] * 16 for _ in range(16)]

    def bfs():
        while queue:
            row, col = queue.popleft()
            
            # 목적지 도달 시 1 반환
            if maze[row][col] == 3:
                return 1

            # 4방향 이동
            for x, y in zip(dx, dy):
                nx, ny = row + x, col + y
                # 미로를 벗어나거나 벽을 만나거나 이미 방문한 포인트라면 continue
                if nx < 0 or nx >= 16 or ny < 0 or ny >= 16 or maze[nx][ny] == 1 or visited[nx][ny]:
                    continue
                # 미로에 해당
                queue.append((nx, ny))
                visited[nx][ny] = True

        # 경로에 도달하지 못할 시 0 반환
        return 0

    print(f'#{test_case} {bfs()}')

# row, col = queue.popleft()
#
# # 목적지 도달 시 1 반환
# if maze[row][col] == 3:
#     return 1
#
# for x, y in zip(dx, dy):
#     nx = row + x
#     ny = col + y
#     # 미로 내의 포인트 or 이동 가능 or 방문하지 않았을 때
#     if 0 <= nx <= 14 and 0 <= ny <= 14 and maze[nx][ny] != 1 and not visited[nx][ny]:
#         queue.append((nx, ny))
#         # 해당 포인트 방문 처리
#         visited[nx][ny] = True