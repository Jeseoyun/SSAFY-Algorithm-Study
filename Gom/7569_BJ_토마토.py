# 7569_BJ_토마토.py

'''

1: 익은 토마토 / 0: 익지 않은 토마토 / -1: 토마토가 없는 칸

- 토마토가 전부 익을 때 까지 걸리는 시간 출력
- 전부 익지 못한다면, -1 출력
- 모든 토마토가 이미 익어져 있다면, 0 출력


2차원 배열로 입력 받고, 3차원 접근 

- 상하좌우 4방향 
- 위,아래 (i,j) : (i+layer,j),(i-layer,j) 


BFS

- 토마토(1) 좌표 전부 큐에 담기

- 한번 돌 때, TIME+1

- 큐가 비었는데, 리스트에 안익은 토마토(0)가 있다면 -1

- 원본 좌표 훼손시켜도 됨

'''

from collections import deque

M,N,L=map(int,input().split())
thr_lst=[]
two_lst=[]

day=0

cnt=N
for k in range(N*L):
    cnt-=1
    two_lst.append(list(map(int,input().split())))

    if cnt==0:
        thr_lst.append(two_lst)
        two_lst=[]
        cnt=N

#print(thr_lst)

# 토마토 좌표
q=deque()

for k in range(L):
    for i in range(N):
        for j in range(M):   
            if thr_lst[k][i][j]==1:
                q.append((k,i,j,0))
 

while q:
    # print(q)
    k,i,j,t=q.popleft()
    
    dij=[(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(1,0,0),(-1,0,0)]
    day=max(day,t)

    # dk: 차원, di: 행, dj: 열
    for dk,di,dj in dij:
        nk,ni,nj=k+dk,i+di,j+dj
    
    # where is fucking depth? This is fucking 3d TOMATO

        if 0<=ni<N and 0<=nj<M and 0<=nk<L:
            if thr_lst[nk][ni][nj]==0:
                q.append((nk,ni,nj,t+1))
                thr_lst[nk][ni][nj]=1  # 익은 토마토로 변경
    

def check_tomato(lst):
    global time

    ans=0

    for i in range(N):
        for j in range(M):
            for k in range(L):
                if thr_lst[k][i][j]==0:
                    ans=-1
                    return ans
    else:
        ans=day  
        
    return ans


print(check_tomato(thr_lst))        
        





