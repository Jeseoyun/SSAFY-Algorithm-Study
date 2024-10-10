N, M = map(int, input().split())
field = [list(input()) for _ in range(N)]

dxy = [(1,0),(-1,0), (0,1), (0,-1)]
visited = [[False] * M for _ in range(N)]
result = []

def dfs(x,y, px, py, cnt):
    if visited[x][y] and cnt >= 4:
        result.append(1)
        return
    visited[x][y] = True
    for dx,dy in dxy:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == field[x][y]:
            # 이전 방향으로 돌아가는 행위 방지
            if [nx, ny] != [px, py]:
                dfs(nx, ny, x, y, cnt+1)

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i,j,i,j,0)

if 1 in result:
    print("Yes")
else:
    print("No")