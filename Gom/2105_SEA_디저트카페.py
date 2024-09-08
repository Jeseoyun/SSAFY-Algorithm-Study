'''
내 생각

1. 처음좌표에서 두번째 우하단 지점, 두번째 좌표에서 세번째 좌하단 지점만 선택한다면, 사각형의 나머지 두변은 고정
-> 사각형이 안되는 것 제외한다면, 갈 수 있는 모든 사각형 탐색

2. 위에서 아래로 첫번째 지점을 정해야 중복 발생 X

3. 방문 표시를 하면서 이미 저장된 디저트 점수가 있다면 return

Q.

- 어떤 알고리즘? 
>> 일단 for문으로 첫번째 줄부터 마지막 한칸 전 줄까지가 첫번째 좌표 탐색 대상
>> DFS로 첫번째 우하단까지 모두 탐색, DFS로 두번째 좌하단 모두 탐색
>> 저장해야할 값: 첫번째 좌표까지 이동거리(D1), 두번째 좌표까지 이동거리(D2), 지나친 곳에 대한 디저트 정보(d_lst), 현재까지 좌표 찍은 지점 >> check(global)에 저장

>> check 안의 각 지점에서 3번째, 4번째 즉, d1, d2만큼 이동해보고 첫 좌표와 동일하다면 ans 갱신

'''



# 1차 _실패

'''
# dfs

# 좌하단,우하단,좌상단,우상단 이동 방향 좌표
dij=[(-1,1),(-1,-1),(1,-1),(1,1)]

# i,j: 좌표 / idx: 꼭짓점 좌표 / d_lst: 디저트 정보 / d1,d2: 두번째 좌표까지 거리, 세번째 좌표까지 거리
def dfs(i,j,idx,d_lst,d1,d2):

    global check

    if idx==0:
        ni,nj=i+dij[0][0],j+dij[0][1]

            
        # 가지치기
        # d_lst 같은 점수있다면 return    
        
        if ni<0 or ni>=N or nj<0 or nj>=N:
            return
        
        # 꼭짓점으로 삼는 녀석과 안삼는 녀석, 하지만 둘다 디저트 정보는 가지고 가야함
        dfs(ni,nj,idx+1,d_lst+[lst[i][j]],d1+1,d2)
        dfs(ni,nj,idx,d_lst+[lst[i][j]],d1+1,d2)

    elif idx==1:
        ni,nj=i+dij[0][0],j+dij[0][1]
        if ni<0 or ni>=N or nj<0 or nj>=N:
            return
        
        # 꼭짓점으로 삼는 녀석과 안삼는 녀석, 하지만 둘다 디저트 정보는 가지고 가야함
        dfs(ni,nj,idx+1,d_lst+[lst[i][j]],d1,d2+1)
        dfs(ni,nj,idx,d_lst+[lst[i][j]],d1,d2+1)

    elif idx==2:
        check.append((i,j,idx,d_lst,d1,d2))


# main
N=int(input())
lst=[list(map(int,input().split())) for _ in range(N)]
check=[]

for i in range(N-1):
    for j in range(N):
        dfs(i,j,0,[lst[i][j]],0,0)

print(check)

'''

# 2차 _ 성공
# 풀이법 

'''
dfs 

1. 방향 안꺽고 유지

2. 방향 꺽고 bent(꺽은 수)+1  

>> bent==4(4번 꺽었을 때), 첫번째 좌표랑 위치가 같다면 ans 갱신 (단, 방문 체크를 통해 중복된 값 없는지 확인)

'''

'''
# dfs
# ci,cj: 현재 좌표 / bent: 꺽은 수 / v: 방문 저장 배열
def dfs(ci,cj,bent,v):
    global ans

    if bent==4:
        return
    
    # 3에서 리턴되면 x, 3번 꺽고 직진해야 시작 좌표 만남
    if bent==3:
        # 시작 좌표와 동일한지 확인
        if ci==si and cj==sj:
            # 중복 값 없는지 확인
            if len(v)==len(set(v)):
                ans=max(ans,len(v))

    ni,nj=ci+dij[bent][0],cj+dij[bent][1]

    if 0<=ni<N and 0<=nj<N:
        dfs(ni,nj,bent+1,v+[lst[ci][cj]])  # 방향 꺽음
        dfs(ni,nj,bent,v+[lst[ci][cj]])  # 킵 고잉


# main
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    lst=[list(map(int,input().split())) for _ in range(N)]
    ans=-1
    dij=[(1,1),(1,-1),(-1,-1),(-1,1)]   # 대각선 이동 방향 인덱스: 우하, 좌하, 좌상, 우상

    for si in range(N-2):
        for sj in range(1,N-1):
            # 방문 배열 첫번째 원소, 시작 좌표 삽입 -> dfs 종료 조건에서 확인하기 위함
            dfs(si,sj,0,[])

    print(f'#{tc}',ans)

'''
# 3차 _ 개선
 
# 수정1)  중복 좌표있으면, dfs호출 안시킴 -> 더느려지는데?
# 수정2)  절반 꺽었을 때 현재 길이의 2배가 현재 저장된 ans보다 작다면 return
'''
# dfs
# ci,cj: 현재 좌표 / bent: 꺽은 수 / v: 방문 저장 배열
def dfs(ci,cj,bent,v):
    global ans

    # 수정2, 두번꺽었는데 2배한 길이가 현재 ans보다 작으면 return
    if bent==2:
        if len(v)*2<ans:
            return
 
    if bent==4:
        return
    
    # 3에서 리턴되면 x, 3번 꺽고 직진해야 시작 좌표 만남
    if bent==3:
        # 시작 좌표와 동일한지 확인
        if ci==si and cj==sj:
            # 중복 값 없는지 확인
            if len(v)==len(set(v)):
                ans=max(ans,len(v))

    ni,nj=ci+dij[bent][0],cj+dij[bent][1]

    if 0<=ni<N and 0<=nj<N:
        #print(lst[ni][nj],v)
        # ? 뭐지 lst[ni][nj]하면 v 원소 접근이 안됨. [lst[ni][nj]] 해야하는데 ?
        # 수정1 -> ? 더 느려지는데?
        #if [lst[ni][nj]] not in v:
        dfs(ni,nj,bent+1,v+[lst[ci][cj]])  # 방향 꺽음
        dfs(ni,nj,bent,v+[lst[ci][cj]])  # 킵 고잉


# main
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    lst=[list(map(int,input().split())) for _ in range(N)]
    ans=-1
    dij=[(1,1),(1,-1),(-1,-1),(-1,1)]   # 대각선 이동 방향 인덱스: 우하, 좌하, 좌상, 우상

    for si in range(N-2):
        for sj in range(1,N-1):
            # 방문 배열 첫번째 원소, 시작 좌표 삽입 -> dfs 종료 조건에서 확인하기 위함
            dfs(si,sj,0,[])

    print(f'#{tc}',ans)

'''

# 4차

# 수정부분 _ ans 갱신 후 return

# dfs
# ci,cj: 현재 좌표 / bent: 꺽은 수 / v: 방문 저장 배열
def dfs(ci,cj,bent,v):
    global ans

    # 수정2, 두번꺽었는데 2배한 길이가 현재 ans보다 작으면 return
    if bent==2:
        if len(v)*2<ans:
            return
 
    if bent==4:
        return
    
    # 3에서 리턴되면 x, 3번 꺽고 직진해야 시작 좌표 만남
    if bent==3:
        # 시작 좌표와 동일한지 확인
        if ci==si and cj==sj:
            # 중복 값 없는지 확인
            if len(v)==len(set(v)):
                ans=max(ans,len(v))
                return

    ni,nj=ci+dij[bent][0],cj+dij[bent][1]

    if 0<=ni<N and 0<=nj<N:
        print(lst[ni][nj],v)
        # ? 뭐지 lst[ni][nj]하면 v 원소 접근이 안됨. [lst[ni][nj]] 해야하는데 ?
        # 수정1 -> ? 더 느려지는데?
        if [lst[ni][nj]] not in v:
            
            print('v 입니다', v)
            dfs(ni,nj,bent+1,v+[lst[ci][cj]])  # 방향 꺽음
            dfs(ni,nj,bent,v+[lst[ci][cj]])  # 킵 고잉
        else:
            print('가지치기 했음 , ')

# 나 이해 못함
# ?? 
# ?? 
# 겉멋 좋았다 


# main
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    lst=[list(map(int,input().split())) for _ in range(N)]
    ans=-1
    dij=[(1,1),(1,-1),(-1,-1),(-1,1)]   # 대각선 이동 방향 인덱스: 우하, 좌하, 좌상, 우상

    for si in range(N-2):
        for sj in range(1,N-1):
            dfs(si,sj,0,[])

    print(f'#{tc}',ans)



