from collections import deque

def bfs(campus, start, visited):
    total_people = 0

    visited[start[0]][start[1]] = 1
    queue = deque([(start[0], start[1])])

    # 상, 하, 좌, 우
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            # 범위 내 아닐 경우 continue
            if not (0 <= nx < n and 0 <= ny < m): continue

            # 이미 방문한 곳이면 continue
            if visited[nx][ny] == 1: continue

            if campus[nx][ny] == 'P':
                total_people += 1
                campus[nx][ny] = 'O'
                queue.append((nx, ny))
                visited[nx][ny] = 1
            elif campus[nx][ny] == 'O':
                queue.append((nx, ny))
                visited[nx][ny] = 1
            else:
                continue

    if total_people == 0:
        return "TT"
    return total_people

# n, m: 캠퍼스의 크기
n, m = map(int, input().split())
campus = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
# print(campus)

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            start = (i, j)

result = bfs(campus, start, visited)

print(result)