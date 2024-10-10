
'''
풀이법 

- 모든 좌표 순회

- 각각의 좌표에서 DFS 수행 : 종료조건 == 시작좌표, dist>=3(최소 사이클 형성 길이)

- 방문 처리 O -> 방문처리된 좌표들에 대해서는 검사할 필요 x

- 디버깅 어캐 함 ???

'''

# MemoryError: Stack overflow
# 뭐가 문젠데 ? ,, ? ,, ? 메모리 일 안함 ? 
# 3가지의 이유가 있었다.



import sys
sys.setrecursionlimit(10**7)

# DFS
def dfs(i,j,target_x,target_y,dist):
    global ans 

    # 이유3 : 사기 코드
    if ans:
        return 

    if i==target_x and j==target_y and dist>=3: # 시작점과 동일하고, 거리가 3이상이라면 
        ans=True
        return

    for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
        ni,nj=i+di,j+dj

        # 이동 기준
        # 1. 시작점과 같은 단어야함
        # 2. 방문처리가 되지 않았고, 같은 단어인 경우 
        # 3. 방문처리가 되었지만, 거리가 3이상인 같은 단어인 경우 (즉, 사이클을 형성한 후의 출발점이라면)
        
        if 0<=ni<N and 0<=nj<M: # 범위 조건 만족 
            if lst[ni][nj]==lst[target_x][target_y]: # 1

                # 이유1: 인덱스 조건을 포함 안시켜주면, 방문처리된 3이상 이동거리 좌표 전부 방문 -> 메모라 초과
                # 이유2(오답으로 이어짐, 시간초과 X): 방문 해제를 안해주면, 시작점이 다른 경우에 대한 처리가 안됨 testcase3
                if (visited[ni][nj]==True and dist>=3 and ni==target_x and nj==target_y) or (visited[ni][nj]==False):  # 2, 3
                    visited[ni][nj]=True # 방문처리
                    dfs(ni,nj,target_x,target_y,dist+1)
                    visited[ni][nj]=False


# Main 
N,M=map(int,input().split())
lst=[list(input()) for _ in range(N)]
visited=[[False for _ in range(M)] for _ in range(N)]
ans=False


for i in range(len(lst)):
    for j in range(len(lst[0])):
        si,sj=i,j  # 시작 좌표 저장
        visited[i][j]=True
        dfs(i,j,si,sj,0)
        visited[i][j]=False

print("Yes" if ans else "No")



# 분류, 회귀 차이
# 로지스틱 회귀 - 장단점
# 앙상블 용어 중요
# train_test_split(x,y,test_size,random_state) 메서드 중요
# scikit-learn example _ regression 개론, 코드 이해하기 
