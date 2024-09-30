

# # 1941 소문난 칠공주

# '''
# DFS 풀이 >> 실패, 첫번째 테스트 케이스 왼쪽에 대한 처리가 일반적인 dfs로 불가


# 완전 탐색 

# - 방문 체크 -> 갔던 장소들에 대해서는 카운트 안하도록 해야 함

# - 시간 초과 문제가 관건일 듯 (?) 


# 가지치기

# - SWEA 최대상금 느낌

# - DFS 호출하고, 남은 인원과 현좌표가 방문체크 리스트에 존재한다면 DFS 호출 안하도록 함 (안씀)

# - 현재 인언 수에서 S에 4명을 더하면, 인원 초과 일때 -> 무조건 안됨

# '''


# # DFS
# # i,j: 좌표 / cnt: 구성원 수 / v: 방문 배열 / sub_lst: 구성원 
# def dfs(i,j,cnt,v,sub_lst,idx_lst):
#     global ans
#     global check

#     # 가지치기

#     if sub_lst.count('Y')>=4: # 구성원 수가 절대 안됨
#         #print(sub_lst)
#         return


#     # 종료 조건 
#     if cnt==7:
#         if sub_lst.count('S')>=4:
#             idx_lst.sort(key=lambda x:(x[0],x[1]))
#             if idx_lst not in check:
#                 check.append(idx_lst)
#                 ans+=1
#                 print(sub_lst)
#         return


#     temp_i,temp_j=i,j

#     for di,dj in dij:
#         ni,nj=i+di,j+dj
        
#         if 0<=ni<N and 0<=nj<N:
#             if v[i][j]==False:
#                 v[i][j]=True
#                 cnt+=1
#                 dfs(ni,nj,cnt,v,sub_lst+[lst[i][j]],idx_lst+[(i,j)])
#                 v[i][j]=False
#                 cnt-=1
#                 i,j=temp_i,temp_j
                


# # Main

# N=5  # 반 크기
# cnt=0  # 인원 수 
# ans=0  # 정답
# check=[] # 방문 좌표 

# # 클래스 입력
# lst=[]
# for _ in range(N):
#     lst.append(list(input()))

# # 방향 좌표
# dij=[(-1,0),(1,0),(0,-1),(0,1)]

# # 방문 체크 배열
# v=[[False for _ in range(N)] for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         dfs(i,j,cnt,v,[],[])


# print(ans)


# # 일반적인 DFS는 분기에 대한 방문이 안됨
# # Test case 2가지 중 왼쪽에 대한 탐색 불가 




##############################################

# DBFS _ 시간초과 실패
# i,j: 좌표 / cnt: 구성원 수 / vis_lst: 방문한 좌표 리스트  

def dfs(i,j,vis_lst,v):
    global ans
    global check

    # 가지치기
    if vis_lst.count('Y')>=4: # 구성원 수가 절대 안됨
        return

    # 종료 조건 
    if len(vis_lst)==7:

        #idx_lst.sort(key=lambda x:(x[0],x[1]))
        vis_lst.sort() # 튜플을 담았기 때문에, sort 한번으로 첫번째 인덱스 두번째 인덱스 차례로 정렬 됨
        
        if vis_lst not in check:
            check.append(vis_lst)
            
            cnt=0
            for i,j in vis_lst:
                if lst[i][j]=='S':
                    cnt+=1
            
            if cnt>=4:
                ans+=1
                #print(vis_lst)
            # print(sub_lst)
        return


    # 현재 방문한 좌표들 차례로 순회
    for i,j in vis_lst:
        # 각 좌표들에 대한 4방향 탐색해서 방문하지 않은 곳으로 dfs 수행
        for di,dj in dij:
            ni,nj=i+di,j+dj    
            if 0<=ni<N and 0<=nj<N:
                if not v[ni][nj]:
                    v[ni][nj]=True
                    dfs(ni,nj,vis_lst+[(ni,nj)],v)
                    v[ni][nj]=False   


# Main

N=5  # 반 크기
ans=0  # 정답
check=[] # 방문 좌표 

# 반정보 입력
lst=[]
for _ in range(N):
    lst.append(list(input()))

# 방향 좌표
dij=[(-1,0),(1,0),(0,-1),(0,1)]

# 방문 체크 배열
v=[[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        v[i][j]=True
        dfs(i,j,[(i,j)],v)
        v[i][j]=False

print(ans)




# 대문어 풀이

'''
- 25개중 7개 선택하는 경우의 수 완탐

- bfs인접조건 + cnt조건 만족 -> ans+1

- 이건 왜 시간초과 안남 ,,? 

'''

