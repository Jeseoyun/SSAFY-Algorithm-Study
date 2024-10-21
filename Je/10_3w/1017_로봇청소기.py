from collections import deque


dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서


def log(arr):
    for lst in arr:
        for elem in lst:
            print(elem, end=" ")
        print()
    print()


def main():
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())  # (r, c): 로봇 청소기가 있는 좌표, d: 방향
    room = [list(map(int, input().split())) for _ in range(N)]  # 0: 청소안됨, 1: 벽

    cleaned = 0
    queue = deque([(r, c, d)])
    while queue:
        x, y, org_d, = queue.popleft()
        # print(x, y, org_d)
        # log(room)

        # 1. 현재 방이 청소되지 않음
        # - 현재 방 청소
        if room[x][y] == 0:
            room[x][y] = 2
            cleaned += 1

        # 2. 현재 칸의 주변 4칸 중 빈 칸이 있는 경우
        # - 반시계 방향으로 90도 회전
        # - 바라보는 방향 기준으로 앞쪽 칸이 청소되지 않은 경우 한 칸 전진
        # - 1로 돌아감
        empty_around = False
        for i in range(4):
            tmp_d = (org_d + 3 - i) % 4
            dx, dy = dxy[tmp_d]
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if room[nx][ny] == 0:  # 청소되지 않은 경우
                queue.append((nx, ny, tmp_d))
                empty_around = True
                break

        # 3. 현재 칸 주변 4칸 중 청소되지 않은 빈 칸이 없음
        # - 방향을 유지한 채 후진 1로 돌아감
        # - 후진할 수 없다면 작동을 멈춤
        if not empty_around:
            back_d = (org_d + 2) % 4
            dx, dy = dxy[back_d]
            bx, by = x + dx, y + dy  # 원래 방향에서 후진

            # 후진할 수 없는 경우 작동을 멈춤
            if bx < 0 or bx >= N or by < 0 or by >= M or room[bx][by] == 1:
                break
            else:
                queue.append((bx, by, org_d))

    print(cleaned)


if __name__ == "__main__":
    main()