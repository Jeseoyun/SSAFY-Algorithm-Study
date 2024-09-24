# https://www.acmicpc.net/problem/1068

def remove_node(node):
    # 삭제된 node는 -2 처리
    parent_list[node] = -2
    # 자식이 있으면 재귀적으로 삭제 처리
    for child in range(len(parent_list)):
        if parent_list[child] == node:
            remove_node(child)

def count_leaf_node(arr, num):
    # 삭제 처리
    remove_node(num)
    # 리프노드 개수 저장 변수
    count = 0
    
    # 삭제처리가 안되어 있고(-2) 자신을 가리키는 자식이 없으면 == 리프노드 카운트 +1
    for i in range(len(arr)):
        if arr[i] != -2:
            if i not in arr:
                count += 1

    return count

N = int(input())
parent_list = list(map(int, input().split()))
del_node_num = int(input())


# 삭제하려는 노드가 루트 노드일때
if del_node_num == parent_list.index(-1):
    print(0)
else:
    print(count_leaf_node(parent_list, del_node_num))