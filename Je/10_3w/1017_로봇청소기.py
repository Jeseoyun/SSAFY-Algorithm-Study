# 1. 현재 칸이 청소되지 않음
# - 현재 칸 청소
# 2. 현재 칸 주변 4칸 중 청소되지 않은 빈 칸이 없음
# - 방향을 유지한 채 후진 1로 돌아감
# - 후진할 수 없다면 작동을 멈춤
# 3. 현재 칸의 주변 4칸 중 빈 칸이 있는 경우
# - 반시계 방향으로 90도 회전
# - 바라보는 방향 기준으로 앞쪽 칸이 청소되지 않은 경우 한 칸 전진
# - 1로 돌아감

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
        print(x, y, org_d)
        log(room)
        if room[x][y] == 0:  # 현재 방이 청소 되어있지 않음
            room[x][y] = 2  # 현재 방 청소
            cleaned += 1

        # 반시계방향으로 돌아가며 주변에 빈 칸이 있는지 검사
        empty_around = False
        for i in range(1, 4):
            tmp_d = (org_d - i) % 4
            dx, dy = dxy[tmp_d]
            nx, ny = x + dx, y + dy
            print("nx, ny", nx, ny)

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if room[nx][ny] == 1:  # 벽인 경우
                continue

            if room[nx][ny] == 0:  # 청소되지 않은 경우
                queue.append((nx, ny, tmp_d))
                empty_around = True
                break

        # 현재 칸 주변 4칸 중 청소되지 않은 빈 칸이 없음
        if not empty_around:
            dx, dy = dxy[org_d]
            nx, ny = x - dx, y - dy  # 원래 방향에서 후진

            # 후진할 수 없는 경우 작동을 멈춤
            if nx < 0 or nx >= N or ny < 0 or ny >= M or room[nx][ny] == 1:
                break

            queue.append((nx, ny, org_d))

    print(cleaned)


if __name__ == "__main__":
    main()