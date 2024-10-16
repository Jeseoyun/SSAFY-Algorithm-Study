# https://www.acmicpc.net/problem/14503 로봇청소기
# 작동 과정
# 1. 청소 안되어 있으면 청소
# 2. 현재 칸 주변 4칸 다 청소 되어 있으면
# -> 바라보는 방향 유지하고 후진할 수 있다면 후진 후 1번
# -> 바라보는 방향의 뒤쪽이 벽이라 후진 못하면 작동 멈춤 / 벽만 아니면 후진 가능
# 3. 청소 안된 빈칸이 있으면
# -> 반시계 방향으로 90도 회전
# -> 앞쪽이 청소 안된게 있으면 앞으로 전진
# -> 1번으로 다시

# 현재 칸 주변 4칸 다 청소 되어 있는지 확인
def is_cleaned(x, y):
    count = 0
    for dx, dy in front_dxy:
        nx, ny = x + dx, y + dy
        if cleaned[nx][ny] == 2 or cleaned[nx][ny] == 1:
            count += 1

    if count == 4:
        return True

    else:
        return False

def solution(x, y, direction):
    global count

    if not cleaned[x][y]:
        cleaned[x][y] = 2
        count += 1

    # 현재 칸 주변 4칸 청소 되어있으면
    if is_cleaned(x, y):
        # 후진
        dx, dy = back_dxy[direction]
        nx, ny = x + dx, y + dy

        # 후진 했는데 벽이면 종료
        if arr[nx][ny] == 1:
            return

        solution(nx, ny, direction)

    else:
        # 방향 회전
        direction -= 1
        if direction < 0:
            direction = 3

        dx, dy = front_dxy[direction]
        nx, ny = x + dx, y + dy

        # 다음 이동 값이 범위 밖이면
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            return

        # # 벽이면 이동 못함
        # if arr[nx][ny] == 1:
        #     return

        # 앞 칸이 청소된 상태면 현재 좌표에서 방향만 바꿔서 진행
        if cleaned[nx][ny] == 2 or arr[nx][ny] == 1:
            solution(x, y, direction)

        else:
            solution(nx, ny, direction)



N, M = map(int, input().split())
# d : 0 북, 1 동, 2 남, 3 서
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 북 동 남 서 이동
front_dxy = ((-1,0), (0,1), (1,0), (0,-1))
back_dxy = ((1,0), (0,-1), (-1,0), (0,1))
cleaned = arr[:]
count = 0

solution(r, c, d)
print(count)