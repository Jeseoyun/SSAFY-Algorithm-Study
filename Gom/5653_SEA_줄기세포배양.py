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


R.

- 문제 1차 해석 40분

- 문제 도전 + 디버깅 - 3,4 시간 -> 실패

- RUN 

'''

import heapq

N,M,K=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
INF=-11 # 세포가 도달할 수 없는 VAL

hq=[]
grid_lst=[]  # 세포 좌표

# 세포 있는 곳
for i in range(N):
    for j in range(M):
        if arr[i][j]!=0:
            val=arr[i][j] 
            time_val=val # 남은 시간
<<<<<<< HEAD
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









=======
            left_time=val # 남은 시간이 0일 때, 활성화 되는 시간
            grid=(i,j)
            grid_lst.append(grid)
>>>>>>> 30ddc79f9e7388151ea47c55c7fdc25b0afe745d

            heapq.heappush(hq,(-val,time_val,left_time,grid))


dij=[(-1,0),(1,0),(0,-1),(0,1)]

print('초기 grid setting',grid_lst)
for _ in range(K):
    sub_hq=[]
    print(_+1)

    while hq:
        
        val,time_val,left_time,grid=heapq.heappop(hq)  # 현재까지 val 음수

        # 문제 발생 - 0에 대한 처리 x, 0이 음수보다 늦게 뽑힘


        if val!=INF:
            time_val-=1

            # 다음 남은 시간이 0 -> VAL최소로 만들어서 MIN 힙 조건으로 가장 빨리 나오게 해주기, TIME_VAL에 임시 VAL 저장
            if time_val==0:
                time_val=-val
                val=INF    # VAL:-11, TIME_VAL: VAL 저장 상태
            heapq.heappush(sub_hq,(val,time_val,left_time-1,grid))  

        # 세포 사망  + 활성화 타임 out - 새로운 녀석 도입
        else:
            if left_time!=0:
                heapq.heappush(sub_hq,(val,time_val,left_time-1,grid))

            else:
                i,j=grid
                print(grid)
                for di,dj in dij:
                    ni,nj=i+di,j+dj
                    new_grid=(ni,nj)

                    # INF에 도달하더라도, time_val 만큼 있어야함 !! 찾았다 ,,, 이 녀석 

                    if new_grid not in grid_lst:
                        heapq.heappush(sub_hq,(-time_val,time_val,time_val,new_grid))
                        grid_lst.append(new_grid)
                        print('new_gird',new_grid)
                        print('현 grid, gird_lst, new_grid',grid,grid_lst,new_grid)

    hq=sub_hq
    print(_+1,'시간 경과 후 hq 상태',hq)    

ans=0
for i in range(len(hq)):
    ans+=hq[i][0]
print('#########',-ans)
