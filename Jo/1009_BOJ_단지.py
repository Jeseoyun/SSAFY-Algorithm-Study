from collections import deque

dxy = [(-1,0), (1,0), (0,-1), (0,1)]

N = int(input())
land = [list(map(int, input())) for _ in range(N)]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    land[x][y] = 0
    cnt = 1

    while queue:
        x,y = queue.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0<=nx<N and 0<=ny<N:
                if land[nx][ny] == 1:
                    land[nx][ny] = 0
                    queue.append((nx,ny))
                    cnt += 1

    return cnt

result = [bfs(i, j) for i in range(N) for j in range(N) if land[i][j] == 1]

print(len(result))
for num in sorted(result):
    print(num)