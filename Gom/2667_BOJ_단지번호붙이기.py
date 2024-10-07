'''
풀이법

DFS 전체 순회


'''

# Main
N=int(input())
lst=[list(map(int,input())) for _ in range(N)]


apt_num=2 # 아파트 단지 번호, 기본 값 1 방문 처리 회피
for i in range(len(lst)):
    for j in range(len(lst[0])):
        if lst[i][j]==1:
            dfs(i,j) # 모두 방문처리 해줌
            apt_num+=1




            




# DFS
def dfs(i,j):

    for di,dj in [(-1,0),(0,-1),(1,0),(-1,0)]:
        ni,nj=i+di,j+dj

        # 범위 안
        if 0<=ni<len(lst) and 0<=nj<len(lst[0]):
     

     
     for i in range(len(lst)):
        for j in range(len(lst[0])):
            dfs(i,j)
