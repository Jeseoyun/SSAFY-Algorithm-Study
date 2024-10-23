from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(start):
    q = deque()
    q.append(start)
    visit[start[0]][start[1]] = True
    count = 1

    while q:
        cur_x, cur_y = q.popleft()
        visit[cur_x][cur_y] = True
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visit[nx][ny] or arr[nx][ny] == 0:
                continue

            q.append((nx, ny))
            visit[nx][ny] = True
            count += 1

    return count

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]
answer = []

for i in range(n):
    for j in range(n):
        if not visit[i][j] and arr[i][j] == 1:
            answer.append(bfs((i, j)))

answer.sort()
print(len(answer))
for i in answer:
    print(i)