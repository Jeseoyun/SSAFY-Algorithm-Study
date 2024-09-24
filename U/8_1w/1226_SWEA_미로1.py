from collections import deque

BOARD_SIZE = 16  # 미로의 크기
end_position = 3

T = 10

# 상 우 하 좌 좌표 이동
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def find_start_point(arr):
    for lst_idx, lst in enumerate(arr):
        for idx, value in enumerate(lst):
            if value == 2:
                return lst_idx, idx


def search(arr, y, x):
    deq = deque()
    deq.append((y, x))  # 루트 노드 삽입

    # 도착 지점에 도착시 종료
    # 시작 지점에서 4방향을 확인하며 갈 수 있는 곳을 확인
    # 4방향을 확인하며 갈 수 있는 좌표라면 deque에 삽입
    while deq:  # 큐에 값이 없을 때까지 반복
        # 부모 노드 pop
        y, x = deq.popleft()
        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]  # 새로 이동할 좌표

            # 새로 이동할 좌표의 값이 1(벽 or 방문한 곳)이라면
            if arr[ny][nx] == 1:
                continue

            # 새 좌표가 리스트 범위를 벗어난 경우 다른 방향의 새로운 좌표를 생성
            if ny > BOARD_SIZE or nx > BOARD_SIZE or ny < 0 or nx < 0:
                continue

            # 새 좌표가 도착 지점인 경우
            if arr[ny][nx] == end_position:
                return 1

            # 위 상황에 모두 포함되지 않을 경우
            # 새 좌표로 이동해도 괜찮음
            # 자식 노드 = 새로 이동할 위치 append
            deq.append((ny, nx))
            # 현재 좌표 방문 표시
            arr[y][x] = 1

    # 큐가 다 비어서 탐색을 종료했음에도
    # 도착지점에 도달하지 못한 경우
    return 0


for _ in range(1, T + 1):
    tc = int(input())
    board = [list(map(int, input())) for _ in range(BOARD_SIZE)]
    # print(board)

    start_y, start_x = find_start_point(board)
    result = search(board, start_y, start_x)

    print(f'#{tc} {result}')