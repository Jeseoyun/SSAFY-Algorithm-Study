
'''

문제 : 사이클 형성 하는 매트릭스 찾기 

풀이법 

- 순차적으로 좌표 접근하며 사이클을 형성하는지 DFS를 통해 확인 하자 

= 시작한 좌표에서 사이클을 형성한 후, 다시 시작좌표로 방문하게 된다면 정답은 TRUE, 아니면 FALSE가 됨

>> 사이클을 형성하고 방문했는지는 어떻게 판별할까? 
   
   DFS로 이동거리(dist)를 인자로 넘겨줌 - 이동거리가 3이상 일때 시작좌표에 도달한다면 사이클을 형성하고 온 거임 _ 불변 사각형 특성  



겪은 어려움

# MemoryError: Stack overflow
# 뭐가 문젠데 ? ,, ? ,, ? 메모리 일 안함 ? 
# 2가지의 이유가 있었다.


Q. 디버깅 어캐 함 ?? 하나 돌릴때 마다 배열 확인하는 거 궁금

'''


# DFS
# i,j: 현재 좌표 / target_x,target_y: 시작 좌표 / dist: 이동거리
def dfs(i,j,target_x,target_y,dist):
    global ans 

    # 이유2 : 사기 코드
    # ans가 True로 바뀐다면 실행중인 DFS 모두 종료 -> 메모리 초과 이유 2
    if ans:
        return 
 

    # 종료조건
    # 시작점과 동일하고 이동거리가 3이상이라면 
    if i==target_x and j==target_y and dist>=3:  
        ans=True
        return


    # 이동 조건
    # 1. 시작점 단어(lst[target_x][target_y]와 같아야 함
    # 2. 1조건 + 방문처리가 되지 않음 
    # 3. 1조건 + 방문처리가 되었지만, 거리가 3이상인 같은 단어인 경우 (즉, 사이클을 형성한 후의 출발점이라면) - 시작점을 방문체크하면 2번 조건으로 인해 방문하지 못하는 문제를 처리하기 위한 예외 조건
    for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
        ni,nj=i+di,j+dj
        
        if 0<=ni<N and 0<=nj<M: # 범위 조건 만족 
            if lst[ni][nj]==lst[target_x][target_y]: # 1조건 : 시작점과 같은 단어 밟아야 함 


                # 2조건: 방문하지 않은 곳
                # 3조건: 방문은 했지만, 사이클을 형성하고 돌아온 경우
                if (visited[ni][nj]==False) or (visited[ni][nj]==True and dist>=3 and ni==target_x and nj==target_y): # dist 조건문에 시작좌표와 같은 좌표에 대해서만 이동해라고 명시되어 있어야 함 -> 명시되어 있지 않다면, 거리가 3이상일 때 시작점 단어와 같다면 방문한곳 전부 DFS 호출 -> 메모리 초과 이유 1
                    visited[ni][nj]=True # 방문처리
                    dfs(ni,nj,target_x,target_y,dist+1)
                    visited[ni][nj]=False # 방문해제 


# 백트랙킹을 반드시 해줘야 함
# TC 3번 
# 시작점이 달라서 사이클이 형성되는 경우에 대한 처리가 안됨


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