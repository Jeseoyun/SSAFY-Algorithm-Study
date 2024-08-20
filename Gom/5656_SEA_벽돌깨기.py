'''
내 생각

- DFS로 모든 범위를 대상으로 종료조건 N 걸고, 부수기 해야함 
- 시간 복잡도: W^N?


구현 함수

- 1. DFS 함수
- 2. 구슬 떨어뜨렸을 때, 연쇄적으로 부숴지고 남은 매트릭스 반환 함수
- 3. 남은 개수 카운트 함수


Point 

2번째 함수


// 35분 
// 2번 함수 구현 생각해보기 -> tomorrow

'''


# N: 기회, W: 폭, H: 높이
N,W,H=map(int,input().split())

lst=[list(map(int,input().split())) for _ in range(H)]
ans=W*H+1

def dfs(mtx,cnt):

    if cnt==N:
        ans=min(ans,check_cnt(mtx))
        return
    
    origin_mtx=mtx

    for i in range(W):
        breaking(mtx,i)
        dfs(mtx,cnt+1)
        mtx=origin_mtx


# 연쇄적으로 부수는 함수
def breaking(mtx,loc):
    pass


def check_cnt(mtx):
    cnt=0   
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if mtx[i][j]!=0:
                cnt+=1

    return cnt

