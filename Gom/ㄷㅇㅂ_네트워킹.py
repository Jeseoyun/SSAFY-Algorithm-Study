'''
- 최단 거리 문제 x

- 완전 탐색 문제 O  >> dfs OK, bfs OK

Q.
- DFS retrun 조건 뭥미 ? DFS 시작 좌표 계산 값이 기존보다 크다면 할필요 없긴함.

- 방문 처리 어떻게 해줘야 함 ? while문 한 방향 진행 좌표들 언제 방문 해제 해야함 ? while문 안에 dfs로 이동 시켜야함 ? 그럼 while문 쓸 필요 없잖아.

- WHILE문 안쓰면 어떻게 방향 바꿈 ? 인덱스+벽 만났을 때 바꿔서 호출? 그럼 종료는 언제? 방문처리는 어떻게 ? 원점 복귀 
'''

# while 도전

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



# only DFS 도전
# 벽이나 범위 탈출 했을 때 방향 바꿔서 수행 할 수 없을듯 ,,?  whilE 써야 하나 ?

def dfs(i,j,dir,dist):

    # 방문 처리
    visited[i][j]=True
    ni,nj=i+dxy[dir][0],j+dxy[dir][1]


    # 네트워크 범위 탈출 + 벽(1) 만남
    # 전 좌표로 이동 시켜주고, 방향 바꾸고, DFS 호출
    # 근데, 방문 처리할때 바깥 범위면 위에 코드에서 애초에 인덱스 에러 나는데 ? 어캐함 ? 가장 앞에 종료 조건 넣어줘야겠지 ?
    if ni<0 or ni>=N or nj<0 or nj>=M or lst[ni][nj]:
        i,j=ni-dxy[dir][0],nj-dxy[dir][1]
        dir=(dir+1)%4
        dfs(i,j,dir,dist-1)

    # 방문 안했다면, 진행 방향 1칸 더 이동
    if not visited[ni][nj]:     
        dfs(ni,nj,dir,dist+1)
        


# Main

# M: row / N: col
M,N=map(int,input().split())   

# network
lst=[list(map(int,input().split())) for _ in range(M)]

# si,sj: start point / ei,ej: end point
si,sj,ei,ej=map(int,input().split())

# 방향 인덱스
dxy=[(-1,0),(1,0),(0,-1),(0,1)]

# 방문 테이블
visited=[[False]*N for _ in range(M)]

# dfs수행
dfs(si,sj,0,0)

# 정답
print(lst[ei][ej])