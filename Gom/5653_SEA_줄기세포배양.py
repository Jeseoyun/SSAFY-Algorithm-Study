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
cell_lst=[]  # 세포 좌표

# 세포 있는 곳
for i in range(N):
    for j in range(M):
        if arr[i][j]!=0:
            val=-arr[i][j] 
            time_val=-val # 남은 시간
            cell_lst.append((i,j))
            heapq.heappush(hq,(-val,time_val,(i,j)))

# # 배양 part
# for _ in range(K):
#     sub_hq=[]


while hq:
    val,time_val,grid=heapq.heappop(hq)
    print(val,time_val,grid)


// 일단 출력 okay

// time out 세포 처리, 인접 조건 확인 후 hq 담기 구현 

// 정답 처리





















