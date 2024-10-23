'''

** 풀이법 **

문제: 도시의 거리가 최소가 되게 만들어라 / 도시의 거리: 모든 가구에서 가장 가까운 치킨 집까지의 거리 총 합

핵심: 폐업을 시키지 않을 치킨집은 어떤 치킨집일까?


Case 1. 치킨 집을 기준으로 가구를 바라본다.

- 치킨집 한 곳과 모든 가구의 거리를 비교할 수는 없음 / 모든 가구가 그 해당 치킨집과 가까운 것은 아니기 때문에

>> 그렇다면, 어떻게 함 ,,?



Case 2. 모든 가구에서 모든 치킨집을 바라본다. 

1. 각 가구에서 모든 치킨 집까지의 거리 정보를 저장함 
2. 정해진 개수 만큼, 조합으로 폐업할 가구 완전탐색 -> 각 경우에서의 도시의 합 구해서 최솟값 반환 

>> 시간초과 날려나 ,,?


[필요정보]
- 치킨집 위치 
- 가구 위치
- 가구당 모든 치킨집 거리 저장할 배열



폐업하지 않을 치킨집을 선택  -> DFS 종료조건
'''

M,N=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(M)]

# 치킨집 거리 정보 
ch_lst=[]
home_num=0 # 가구 수
ans=1e9 # 정답

for i in range(len(lst)):
    for j in range(len(lst[0])):
        if lst[i][j]==2:
            ch_lst.append((i,j))
        
        # 가구면 가구 숫자 +1
        if lst[i][j]==1:
            home_num+=1


# 가구-치킨 거리정보 테이블
dist_lst=[[] for _ in range(home_num)]


# 거리 계산
row=0
for i in range(len(lst)):
    for j in range(len(lst[0])):
        if lst[i][j]==1:
            for k in range(len(ch_lst)):
                ch_i,ch_j=ch_lst[k][0],ch_lst[k][1]
                dist=abs(i-ch_i)+abs(j-ch_j)
                dist_lst[row].append(dist)
            row+=1
                
print(dist_lst)

############ 여기까지 ok


# DFS
def dfs(check,idx):
    global ans
    
    # 종료조건
    if len(check)==N:
        
        ### 완탐으로 어떤거 삭제할지 구현
        ### 제외한 컬럼 빼고 최단 거리구하는 코드 작성
        total_dist=0

        for i in range(len(lst)):
            dist=1e9
            for j in range(len(lst[0])): 
                if j in check:
                    dist=min(dist,lst[i][j])
            
            total_dist+=dist

        # print('#########',check)
        # print(total_dist)

        ans=min(ans,total_dist)
        print(check)
        return


    if idx==len(dist_lst):
        return

    dfs(check,idx+1)
    dfs(check+[idx],idx+1)


dfs([],0)
print(ans)