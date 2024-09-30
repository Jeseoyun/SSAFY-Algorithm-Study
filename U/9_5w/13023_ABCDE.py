'''
https://www.acmicpc.net/problem/13023
신장트리인지 확인하는 문제
사이클이 있다면 신장트리가 아님
사이클이 있다? => 간선의 수가 노드의 수 -1보다 크다는 의미
-----
문제를 잘못 이해함
A->B->C->D->E의 관계가 있는지 확인
5명이 이런 관계를 갖기만 하면 됨
'''
from collections import defaultdict

N, M = map(int, input().split())

# 노드 수가 4개 이하라면 해당 관계가 생길 수 없음
if N < 4:
    print(0)
    quit()

relations = defaultdict(list)
visited = set()
result = 0

for i in range(M):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

# print(relations)


def search(current_node, visited, depth):
    # 간선을 4번 이상 이을 수 있으면
    if depth >= 4:  return depth


    # 현재 노드의 인접 노드로
    for adj_node in relations[current_node]:
        if adj_node in visited: continue

        # visited check
        visited.add(adj_node)
        res = search(adj_node, visited, depth+1)
        visited.remove(adj_node)
        if res >= 4:
            return res

    return depth


# 모든 노드에 대해서 해당 관계가 있는지 확인
for search_node in relations.keys():
    visited.add(search_node)
    result = search(search_node, visited, 0)
    visited.remove(search_node)
    if result >= 4:
        print(1)
        quit()

if result < 4:
    print(0)