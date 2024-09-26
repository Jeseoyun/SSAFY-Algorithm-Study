
# BFS 풀이

from collections import deque

# bfs
def bfs(st_point):
    # 큐 생성, 시작 노드 삽입
    q=deque()
    q.append(st_point)

    # 이동 방향 좌표
    dxy=[(-1,0),(1,0),(0,-1),(0,1)]  

    # 큐가 빌때 까지 반복
    while q:
        # 큐 최상단의 노드 좌표 추출
        x,y,=q.popleft()

        # 4방향으로 이동하며 조건 확인, 만족 시 큐에 삽입
        for dx,dy in dxy:
            nx,ny=x+dx,y+dy

            # 범위 조건 + 좌표 이동 여부
            if 0<=nx<16 and 0<=ny<16 and lst[nx][ny]!=1:
                # 도착점이라면 ans 갱신, 함수 종료
                if lst[nx][ny]==3:
                    return True

                # 방문체크 + 큐 삽입
                lst[nx][ny]=1
                q.append((nx,ny))

    # 큐가 빌때가
    return False
    


# main
T=10
for tc in range(1,T+1):
    N=int(input())
    lst=[list(map(int,input())) for _ in range(16)]

    # 시작점, 도착점
    st_point,end_point=(1,1),(11,11)


    if bfs(st_point):
        print(f'#{tc}',1)
    else:
        print(f'#{tc}',0)


#########################################

# DFS 풀이

# dfs
def dfs(x, y, lst):
    global ans

    # 종료 조건 - 3 발견
    if lst[x][y] == 3:
        ans = 1
        return

    lst[x][y] = 1  # 방문처리

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 16 and 0 <= ny < 16:
            if lst[nx][ny] == 0 or lst[nx][ny] == 3:
                dfs(nx, ny, lst)

    return



# main
T=10
for _ in range(1,T+1):
    t=int(input())
    lst=[list(map(int,input())) for _ in range(16)]

    # 도달유무
    ans=0

    # 시작점
    x_idx,y_idx=1,1

    # 방향 이동 좌표
    dxy=[(1,0),(-1,0),(0,1),(0,-1)]

    dfs(x_idx,y_idx,lst)
    print(f'#{t}',ans)


