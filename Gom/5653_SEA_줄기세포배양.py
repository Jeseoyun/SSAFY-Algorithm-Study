'''

K시간 뒤에 활성화+비활성화 상태 줄기 세포의 개수?


내 생각

- 초기 세팅

- (origin_src,time_src,(x,y))  # 원래 점수, 깍인 점수, 좌표


1. 초기 정보들 방문 처리하고 힙(max_heapq)에 삽입


- 동작 과정

1. 원래 점수가 높은거 부터 힙에서 빼주기

2. 현재 점수가 0이면, 주변 좌표값 확인하고,

- 시간이 끝난 좌표는 별도의 리스트에 좌표 저장해두기

3. 만약에 세포가 없는 자리라면, 큐에 방향 변경 정보 확인해서 삽입해주기


Q.

1. K 시간 만큼 지나게 하려면 어캐 구현 해야함 ? N번 꺼내고 다시 N(최대N)번 삽입? 원형 Q?

2. 이젠 나도 모르겠다. 해보자 


문제 1차 해석 40분

'''

import heapq

N,M,K=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

hq=[]
grid_lst=[]  # 세포 좌표

# 세포 있는 곳
for i in range(N):
    for j in range(M):
        if arr[i][j]!=0:
            val=arr[i][j] 
            time_val=val # 남은 시간
            grid=(i,j)
            grid_lst.append(grid)
            heapq.heappush(hq,(-val,time_val,grid))

print('initial hq',hq)
dij=[(-1,0),(1,0),(0,-1),(0,1)]

for _ in range(K):
    sub_hq=[]
    while hq:
        
        val,time_val,grid=heapq.heappop(hq)  # 현재까지 val 음수
        
        if time_val!=0:
            time_val-=1
            heapq.heappush(sub_hq,(val,time_val-1,grid))


        else:
            i,j=grid
            for di,dj in dij:
                ni,nj=i+di,j+dj
                new_grid=(ni,nj)
                if new_grid not in grid_lst:
                    heapq.heappush(sub_hq,(val,-val,new_grid))
                    grid_lst.append(new_grid)

        print('##',grid)
        print('##',hq)
    
    hq=sub_hq
    print(_+1)
    print('gird_lst',grid_lst)
    print('hq',hq)

ans=0
for i in range(len(hq)):
    ans+=hq[i][0]
    print('#########',-ans)





















