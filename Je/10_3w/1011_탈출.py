# https://www.acmicpc.net/problem/3055

# . : 비어있음
# * : 물 (못지나간다)
# X : 돌 (모찌나간다)
# D : 비버 굴 (도착지점)
# S : 고슴도치 (출발지점)

# 조건
# 1. 고슴도치는 상하좌우 중 지나갈 수 있는 지점 하나로 이동 가능
# 2. 물이 차있는 칸과 인접한 칸은 계속 물이 차게됨 (비버 굴에는 물이 차지 않는다)

# 구해야 할 것
# 비버의 굴로 이동하기 위한 최소 시간

# 방법
# 고슴도치 위치도 bfs로 옮겨다녀야 하고, 물도 bfs로 채워넣어야 함
# 고슴도치가 한 번 이동할 때마다 map 모양 바꿔줘야 함

# troubleshooting
# 1분마다 물이 퍼져나가야하는데 큐를 기준으로 돌려버리니까 1분마다 map이 바뀌는걸 구현하는게 어렵다


from collections import deque


dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def log(arr):
    for lst in arr:
        for elem in lst:
            print(elem, end=" ")
        print()
    print()


def get_pos(tw_map, r_size, c_size, target):
    target_pos = []
    for i in range(r_size):
        for j in range(c_size):
            if tw_map[i][j] == target:
                target_pos.append((i, j))
    return target_pos


def flood(tw_map, r_size, c_size, water_pos_li):
    for pos in water_pos_li:
        x, y = pos
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= r_size or ny < 0 or ny >= c_size:
                continue

            # 비어 있는 칸이면 물로 바꿔줌
            if tw_map[nx][ny] == ".":
                tw_map[nx][ny] = "*"


def dochi_move_bfs(tw_map, r_size, c_size, start_pos):
    sx, sy = start_pos
    dochi_queue = deque([])
    dochi_queue.append((sx, sy, 0))

    visited = [[0]*c_size for _ in range(r_size)]
    visited[sx][sy] = 1

    prev_move_cnt = -1

    while dochi_queue:
        x, y, dochi_move_cnt = dochi_queue.popleft()
        # print((x, y), "->", tw_map[x][y], dochi_move_cnt)

        # 다음에 물이 넘치는 지역 표시
        if dochi_move_cnt > prev_move_cnt:
            water_pos_li = get_pos(tw_map, r_size, c_size, "*")
            flood(tw_map, r_size, c_size, water_pos_li)
            prev_move_cnt = dochi_move_cnt
            # print("map:")
            # log(tw_map)

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= r_size or ny < 0 or ny >= c_size:
                continue
            if visited[nx][ny]:
                continue

            # 비버의 소굴에 도착한 경우
            if tw_map[nx][ny] == "D":
                # print("도오챠크")
                return dochi_move_cnt + 1

            if tw_map[nx][ny] != ".":
                continue

            dochi_queue.append((nx, ny, dochi_move_cnt+1))
            visited[nx][ny] = 1
            # print("visited:")
            # log(visited)

    return "KAKTUS"


def main():
    R, C = map(int, input().split())
    tw_map = [list(input()) for _ in range(R)]

    # 고슴도치, 물 처음 위치 찾기
    start_pos = get_pos(tw_map, R, C, "S")[0]  # S는 하나만 입력됨

    result = dochi_move_bfs(tw_map, R, C, start_pos)
    print(result)


if __name__ == "__main__":
    main()