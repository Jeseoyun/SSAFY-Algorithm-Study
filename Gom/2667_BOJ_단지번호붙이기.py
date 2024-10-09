'''
풀이법

1. DFS로 인접한 아파트를 묶어주고 번호로(apt_num) 그룹화 한다.

2. 단지 개수를 별도의 리스트(ans_lst)에 담고 그룹화 한다.

3. 출력한다.

'''
# DFS
# i,j: 좌표 / cnt: 가구 개수
def dfs(i,j):

    for di,dj in [(-1,0),(0,-1),(1,0),(0,1)]:
        ni,nj=i+di,j+dj

        # 범위 안
        if 0<=ni<len(lst) and 0<=nj<len(lst[0]):
            if lst[ni][nj]==1:
                lst[ni][nj]=apt_num
                dfs(ni,nj)

# Main
N=int(input())
lst=[list(map(int,input())) for _ in range(N)]
ans_lst=[]

apt_num=2 # 아파트 단지 번호, 기본 값 1 방문 처리 회피
for i in range(len(lst)):
    for j in range(len(lst[0])):
        if lst[i][j]==1:
            lst[i][j]=apt_num
            dfs(i,j) # 모두 방문처리 해줌
            apt_num+=1


# masic method : sum
# https://wellsw.tistory.com/210 : 2 mtx -> 1 mtx

lst_flat = list(sum(lst, []))
for apt_num in range(2,apt_num):
    ans_lst.append(lst_flat.count(apt_num))

print(len(ans_lst))
for num in sorted(ans_lst):
    print(num)



            





     
