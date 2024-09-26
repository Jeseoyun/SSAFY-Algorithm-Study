'''
https://www.acmicpc.net/problem/1068
'''
from collections import defaultdict

N = int(input())

arr = list(map(int, input().split()))
remove_node = int(input())

root_node = arr.index(-1)
# 만약 제거하는 노드가 부모 노드라면 바로 0 반환
if remove_node == root_node:
    print(0)
    quit()

tree = defaultdict(list)
leaf_cnt = 0

# 딕셔너리로 변환
for idx, parent in enumerate(arr):
    # 부모가 없다면 => 루트 노드
    if parent == -1:
        continue

    tree[parent].append(idx)

# print(tree)


# 1. 트리 완전 탐색하기 - 깊이 우선
def search(t, node_idx):
    # print(node_idx)
    global leaf_cnt

    # 자식이 없는 노드의 경우 딕셔너리에 키가 생성되지 않음
    # 자식이 없다면 value가 비어있음
    # 해당 노드에 자식이 없다면 리프노드 수 +1
    if node_idx not in t.keys() or not t[node_idx]:
        leaf_cnt += 1
        return

    # 여기 도달한 것은 자식이 있다는 의미
    # 해당 노드의 자식노드로 들어감
    for child_node in t[node_idx]:
        search(t, child_node)


# 2. 제거할 노드 연결을 끊어주기
# 부모 리스트에서 해당 노드 제거
parent_node = arr[remove_node]
tree[parent_node].remove(remove_node)

# 시작은 루트 노드부터
search(tree, root_node)
print(leaf_cnt)