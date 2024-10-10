# 13023 BOJ ABCDE
# 문제 설명 더러움 
# 결론: 한붓그리기 5개 노드 okay면 True 출력하기


# 1. 그래프 초기화
# DFS
def dfs(nod,lst):
    global ans

    if len(lst)==5:    
        ans=True
        return
    
    for nex_nod in graph[nod]:
        if visited[nex_nod] == False:
            visited[nex_nod]=True
            dfs(nex_nod,lst+[nex_nod])
            visited[nex_nod]=False

# Main
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
visited=[False for _ in range(N+1)]
ans=False

for _ in range(M):
    nod1,nod2=map(int,input().split())

    # 양방향 간선
    graph[nod1].append(nod2)
    graph[nod2].append(nod1)

for nod in range(N+1):
    visited[nod]=True
    dfs(nod,[nod])
    visited[nod]=False
    
    # magic code -> 안해주면 시간초과 나는 마술 
    # 순차적으로 노드를 탐색하면서 True값을 뽑았다면, 이후 노드들에 대해 탐색 x
    if ans:
        break

if ans:
    print(1)
else:
    print(0)


##################################

# 2. defaultdic

from collections import defaultdict

# DFS
def dfs(nod,lst):
    global ans

    if len(lst)==5:    
        ans=True
        return
    
    for nex_nod in dic[nod]:
        if visited[nex_nod] == False:
            visited[nex_nod]=True
            dfs(nex_nod,lst+[nex_nod])
            visited[nex_nod]=False


# MAIN
N,M=map(int,input().split())
dic=defaultdict(list)
visited=[False for _ in range(N+1)]
ans=False

# 그래프 형성
for _ in range(M):
    n1,n2=map(int,input().split())
    dic[n1].append(n2)
    dic[n2].append(n1)

# 각 지점에서 DFS 수행
for nod in range(N+1):
    visited[nod]=True
    dfs(nod,[nod])
    visited[nod]=False

    # magic method
    if ans:
        break

if ans:
    print(1)
else:
    print(0)


# 1, 2 시간 비슷
# GPT bro 소환 