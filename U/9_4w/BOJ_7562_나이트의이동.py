'''
https://www.acmicpc.net/problem/7562

흠... bfs인 느낌
'''
from collections import deque
dyx =[(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

T = int(input())


def move_knight(y, x, move_cnt):
    visited = set()
    deq = deque([(y, x, move_cnt)]) # 시작 좌표 넣기

    while deq:
        cy, cx, total_move_cnt = deq.popleft()

        # 현재 좌표가 도착 좌표라면 끝내기
        if cy == target_y and cx == target_x:
            return total_move_cnt

        # 방문한 적 있는 좌표라면 넘어가기
        if (cy, cx) in visited: continue

        visited.add((cy, cx))

        for dy, dx in dyx:
            ny, nx = cy+dy, cx+dx

            # 범위를 밖이면 다음으로
            if ny < 0 or ny >= BOARD_SIZE or nx < 0 or nx >= BOARD_SIZE: continue

            deq.append((ny, nx, total_move_cnt+1))

    return -1


for _ in range(1, T+1):
    BOARD_SIZE = int(input())
    start_y, start_x = map(int,input().split())
    target_y, target_x = map(int, input().split())
    # print(start_y,start_x)
    # print(target_y, target_x)

    result = move_knight(start_y, start_x, 0)

    print(result)