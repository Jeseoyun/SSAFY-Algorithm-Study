from collections import deque

dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]


# def func(x, y, count):
#     global answer
#     if count > answer:
#         return
#     if x == end_x and y == end_y:
#         answer = min(answer, count)
#         return
#     for i in range(8):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx < 0 or nx >= n or ny < 0 or ny >= n:
#             continue
#         if visit[nx][ny]:
#             continue
#
#         visit[nx][ny] = True
#         func(nx, ny, count + 1)
#         visit[nx][ny] = False


tc = int(input())

for i in range(tc):
    answer = 12345678
    n = int(input())  # 체스판 한변의 길이
    visit = [[-1] * n for i in range(n)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    visit[start_x][start_y] = 0
    flag = True
    # func(start_x, start_y, 0)
    q = deque()
    q.append((start_x, start_y))

    while q and flag:
        cur_x, cur_y = q.popleft()
        for i in range(8):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visit[nx][ny] != -1:
                continue

            q.append((nx, ny))
            visit[nx][ny] = visit[cur_x][cur_y] + 1
            if nx == end_x and ny == end_y:
                flag = False
                break

    print(visit[end_x][end_y])