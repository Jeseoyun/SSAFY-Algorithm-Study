# 7562 나이트의 이동

# dfs
# ?? What PBL?  >>  시간 초과 issue

'''
def dfs(i,j,cnt):
    global ans

    #print(i,j)


    # 도착점 도착
    if lst[i][j]==2:
        ans=min(ans,cnt)
        # print('check')
        return
    
    di = [-1, 1, 2, 2, 1, -1, -2, -2]
    dj = [2, 2, 1, -1, -2, -2, -1, 1]

    for k in range(8):
        ni,nj=i+di[k],j+dj[k]
        
        # 체스판 out
        if 0<=ni<N and 0<=nj<N:
            if visited[ni][nj]!=1: # 방문하지 않았다면
                visited[ni][nj]=1 # 방췍
                dfs(ni,nj,cnt+1) 
                visited[ni][nj]=0


# main
N=int(input())
lst=[[0 for _ in range(N)] for _ in range(N)] # 체스판
visited=[[0 for _ in range(N)] for _ in range(N)] # 방문체크 배열

si,sj=map(int,input().split())
ei,ej=map(int,input().split())

lst[ei][ej]=2 # 도착점

ans=1e9
cnt=0 
dfs(si,sj,cnt)

print(ans)

'''



# BFS풀이 1
# python3 말고 pypy 돌려야 시초 안뜸 
# What PBL ..?  방췍 리스트 이슈

'''
bfs를 사용해야 하는 이유

- 4방향 탐색이 아닌 8방향 탐색 -> 시간 복잡도 훨씬 큼

- bfs로 한번 이동한 좌표 -> 현좌표에서 한번 이동했을 때 갈 수 있는 최선의 좌표가 보장 됨

'''

'''
from collections import deque
import sys
input = sys.stdin.readline

# main
TC=int(input())

for _ in range(TC):
    
    N=int(input()) # 체스판 가로 길이
    si,sj=map(int,input().split()) # 시작점
    ei,ej=map(int,input().split()) # 목표점

    lst=[[0 for _ in range(N)] for _ in range(N)] # 체스판
    visited=[[0 for _ in range(N)] for _ in range(N)] # 방췍 배열
    
    q=deque()
    q.append((si,sj))
    visited[si][sj]=True # 시작점 방췍

    # bfs
    while q:
        i,j=q.popleft()

        # 나이트 이동방향
        di = [-1, 1, 2, 2, 1, -1, -2, -2]
        dj = [2, 2, 1, -1, -2, -2, -1, 1]

        for k in range(8):
            ni,nj=i+di[k],j+dj[k]

            if 0<=ni<N and 0<=nj<N:
                if visited[ni][nj]!=True:
                    q.append((ni,nj))
                    visited[ni][nj]=True
                    lst[ni][nj]=lst[i][j]+1

    # print(lst)
    print(lst[ei][ej])

'''


# BFS 풀이2

# 개선
# 1. while문에서 목표점 도달 시 탈출  
# 2. 방문 체크 안사용해도 됨 -> BFS의 한번 이동은 최적해가 보장 되기 때문에 방문한 좌표에 대해서 더 이상 갱신이 일어나지 않음 -> 원본 테이블만 활용해서 사용하자

# Python3 통과
# pypy _ 1번 풀이: 440ms / 2번 풀이: 364ms

from collections import deque
import sys
input = sys.stdin.readline


# bfs
def bfs():

    q=deque()
    q.append((si,sj))
    lst[si][sj]=1 # 시작점 방췍

    # bfs
    while q:
        i,j=q.popleft()

        if i==ei and j==ej:
            return lst[i][j]-1  # 처음 좌표(이동안했기 때문에 원래 0인데 방문처리 때문에 1로 시작함)를 1로 넣었으므로 이동횟수 1감소


        # 나이트 이동방향
        di = [-1, 1, 2, 2, 1, -1, -2, -2]
        dj = [2, 2, 1, -1, -2, -2, -1, 1]

        for k in range(8):
            ni,nj=i+di[k],j+dj[k]

            if 0<=ni<N and 0<=nj<N:
                if lst[ni][nj]==0:
                    q.append((ni,nj))
                    lst[ni][nj]=lst[i][j]+1

    return lst[ei][ej]


# main
TC=int(input())

for _ in range(TC):
    
    N=int(input()) # 체스판 가로 길이
    si,sj=map(int,input().split()) # 시작점
    ei,ej=map(int,input().split()) # 목표점
    lst=[[0 for _ in range(N)] for _ in range(N)] # 체스판
    ans=bfs()  # bfs 실행
    
    print(ans) 

