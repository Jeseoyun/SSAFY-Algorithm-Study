# 1068 트리

'''
[고민거리]

1. 그래프 표현 방법

2. 노드 가지 자르기 

3. 리프 노드 개수 카운트



[생각 해보기]

1. 자르는 노드를 기준으로 DFS탐색 -> 갈 수 있는 모든 노드 방문

>> 방문한 노드들 : 없어질 노드들

2. 나머지 노드들에 대해 리프노드 찾기

   1) 방문한 노드들을 제외하고, 다시 트리 그려보자
   2) 리프노드 개수 = (방문체크 된 노드) - (새로 만든 트리의 키 개수)  
   
   * 단, 최상단 노드의 키 값이 -1인 경우 제외해줘야 함 - 존재하지 않는 노드이므로

'''

from collections import defaultdict

# DFS
def dfs(nod):

    for nxt_nod in dic1[nod]:
        if not v[nxt_nod]:
            v[nxt_nod]=True
            dfs(nxt_nod)

    return 


# MAIN
# 노드 개수
N=int(input())
lst=list(map(int,input().split()))

# 자를 노드
del_nod=int(input())

# 부모 노드 정보 딕셔너리
dic1=defaultdict(list)
dic2=defaultdict(list)

# 방문 리스트
v=[False for _ in range(N)]

for i in range(len(lst)):
    node,idx=lst[i],i
    dic1[node].append(i)


v[del_nod]=True # 시작점 방문처리
dfs(del_nod) # DFS 수행


# 제외된 노드 개수(방문하지 않는 노드)
cnt1=v.count(True)

for i in range(len(v)):
    if v[i]:
        pass
    else:
        node,idx=lst[i],i
        dic2[node].append(i)
            

# 전부 True로 바뀐 경우 +1 (x), 0출력
if v.count(True)==N:
    print(0)


# 최상단 루트노드(-1) 카운트 빼진거 1 더해줌 
else:
    print(N-cnt1-len(dic2.keys())+1)
    


