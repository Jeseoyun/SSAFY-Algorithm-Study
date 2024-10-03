'''
- 최단 거리 문제 x

- 완전 탐색 문제 O  >> dfs OK, bfs OK

Q.
- DFS retrun 조건 뭥미 ? DFS 시작 좌표 계산 값이 기존보다 크다면 할필요 없긴함.

- 방문 처리 어떻게 해줘야 함 ? while문 한 방향 진행 좌표들 언제 방문 해제 해야함 ? while문 안에 dfs로 이동 시켜야함 ? 그럼 while문 쓸 필요 없잖아.

- WHILE문 안쓰면 어떻게 방향 바꿈 ? 인덱스+벽 만났을 때 바꿔서 호출? 그럼 종료는 언제? 방문처리는 어떻게 ? 원점 복귀 
'''

# 1차 실패 __ 감도 안옴

'''
# i,j: 좌표 / dir: 방향 인덱스 / dist: 이동거리 
def dfs(i,j,dir,dist):

    # 방문 처리
    visited[i][j]=True
    ni,nj=i+dxy[dir][0],j+dxy[dir][1]

    while True:
        # 네트워크 범위 탈출 
        if ni<0 or ni>=N or nj<0 or nj>=M:
            break
        
        # 벽(1) 만남
        if lst[ni][nj]:
            break

        # 방문 안했다면, 진행 방향 1칸 더 이동
        if not visited[ni][nj]:     
            dfs(ni,nj,dir,dist+1)
        
    # 좌표 원위치 -> 탈출 당시: 인덱스 밖 or 벽 속
    i,j=ni-dxy[dir][0],nj-dxy[dir][1]
    
    # 방향 변경, DFS 수행
    dir=(dir+1)%4

    for k in range(len(dir)):
        dfs(ni,nj,k,dist)

'''


'''
2차 코칭

- 모든 좌표에 대해서 방문 처리를 하는게 아님. 방문처리 개념이랑 조금 다름

- 벽이나 모서리 앞, 방향을 바꿔야하는 경우에 대해서만 생각하면 됨. 지나온곳을 다른 곳들을 지나쳐 더 나은 최적해에 도달할 수 있음.

>> 멈출 수 없는 좌표 존재, 문제에서 말하는 도달할 수 없는 경우인 곳, -1

>> 벽, 모서리 한칸 앞 좌표에 대해서만 방문처리를 하고, dfs를 호출할지 안할지 따짐 - 최적값 테이블(visited) 필요

'''


def dfs(position, dist):
    # 현재 좌표
    # x, y는 범위 밖이나 벽 직전의 좌표가 나올 수 밖에 없음 -> dfs를 그때만 호출하므로
    x, y = position

    # 방문한적 있는데 현재 파라미터 dist보다 최단거리가 저장되어 있는 경우 -> dfs 죽이기
    if visited[x][y] != -1 and dist >= visited[x][y]:
        return

    # dist 갱신 _ 방문한적 없거나, 방문한적 있는데 기존보다 더 최단거리 값을 가지고 있는 경우
    visited[x][y] = dist

    for dx, dy in dxy:
        sub_dist = 0    # 한쪽 방향 이동거리
        tmpX, tmpY = x, y  # 현재 위치 임시저장 

        while True:
            tmpX, tmpY = tmpX + dx, tmpY + dy

            # 네트워크 범위 밖
            if tmpX < 0 or tmpX >= M or tmpY < 0 or tmpY >= N: 
                break
            
            # 벽인 경우
            if lst[tmpX][tmpY]:
                break
            
            # 거리 +1
            sub_dist += 1
        
        tmpX, tmpY = tmpX - dx, tmpY - dy  # 한칸 전으로 돌려주기

        # 방문처리 하지 않는 이유: 지나온 좌표를 거쳐 더 나은 최단 거리가 나올 수 있기 때문에, 종료 조건은 dfs 첫 부분에서 걸어줌
        # 움직인 거리가 0이라면 dfs 호출할 필요x, 이동한 경우에 대해서만 dfs 호출
        if sub_dist:
            dfs((tmpX, tmpY), dist + sub_dist)
        

# Main
T = int(input())
for tc in range(1, T + 1):
    M, N = map(int, input().split())

    # 네트워크
    lst = [list(map(int, input().split())) for _ in range(M)]

    # 시작점, 도착점
    si, sj, ei, ej = map(int, input().split())

    # 방향
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 최단거리 정보 테이블
    visited = [[-1 for _ in range(N)] for _ in range(M)]

    # 시작점에서 dfs 수행
    dfs((si, sj), 0)

    #b result = visited[ei][ej] if visited[ei][ej] != -1 else -1
    print(f'#{tc} {visited[ei][ej]}')