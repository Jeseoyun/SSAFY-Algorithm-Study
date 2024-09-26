'''
내 생각

- DFS로 모든 범위를 대상으로 종료조건 N 걸고, 부수기 해야함 
- 시간 복잡도: W^N?


구현 함수

- 1. DFS 함수
- 2. 구슬 떨어뜨렸을 때, 연쇄적으로 부숴지고(bfs) 남은 매트릭스 반환 함수(pull_mtx)
- 3. 남은 개수 카운트 함수


Point - 2번째 함수

>> BFS (INDEX, BLCOK_NUM) 수행 + 내려주기

'''


import copy
from collections import deque


# 남은 블록 반환함수 
def check_cnt(mtx):
    cnt=0   
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if mtx[i][j]!=0:
                cnt+=1

    return cnt


# 벽돌 내리기 함수
def down_block(mtx):
    new_mtx = [[0] * W for _ in range(H)]
    for w in range(W):
        init = H - 1
        for h in range(H - 1, -1, -1):
            if mtx[h][w]:
                new_mtx[init][w] = mtx[h][w]
                init -= 1

    return new_mtx


def dfs(mtx,cnt):
    global ans

    # 기회 소진 시 종료
    if cnt==N:
        ans=min(ans,check_cnt(mtx))
        return

    # 벽돌이 있는 좌표에 대해 BFS수행, 부수고 원본 배열 복귀
    for i in range(H):
        for j in range(W):
            if mtx[i][j]:
                
                # 원본 배열 저장
                origin_mtx=copy.deepcopy(mtx)
                
                # BFS
                q=deque([(i,j,mtx[i][j])])
                while q:
                    i,j,num=q.popleft()
                    mtx[i][j]=0

                    # 크기만큼 4방향으로 탐색하며 파괴 
                    for k in range(1,num):
                        for di,dj in dij:
                            ni,nj=i+di*k,j+dj*k

                            # 범위 체크 + 벽돌 유무, 앞 전에 처리된 블록일 수 있으니 현재 q에 존재하는지 확인
                            if 0<=ni<H and 0<=nj<W and mtx[ni][nj]!=0:
                                if (ni,nj,mtx[ni][nj]) not in q:
                                    q.append((ni,nj,mtx[ni][nj]))

                down_mtx=down_block(mtx)
                dfs(down_mtx,cnt+1)
                mtx=origin_mtx



# main

# N: 기회, W: 폭, H: 높이
N,W,H=map(int,input().split())
mtx=[list(map(int,input().split())) for _ in range(H)]
ans=1e9
dij=[(-1,0),(1,0),(0,-1),(0,1)]
dfs(mtx,0)
print(ans)



# H=4
# W=5

# lst=[[1,1,0,1,1],
#      [1,1,1,0,0],
#      [0,0,1,0,0],
#      [1,0,0,0,1]]

# for i in range(len(p_mtx)):
#     print(p_mtx[i])
