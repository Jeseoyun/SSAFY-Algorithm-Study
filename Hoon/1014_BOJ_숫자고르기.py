# 이걸 그래프 발상을 어케함?
max_li = set()

def dfs(graph, cur_node, dist):
    global max_li
    # print("위치: ",cur_node)

    for next_node in graph[cur_node]:
        #왔던길 포함 사이클이면?
        if next_node in dist:
            # print(cur_node, next_node, dist)
            for i in dist:
                max_li.add(i)
            continue

        dist.add(next_node)
        dfs(graph, next_node, dist)
        dist.remove(next_node)
    return


def main():
    global max_li

    node_num = int(input())
    graph = [[] for _ in range(node_num + 1)]

    for i in range(node_num):
        node = int(input())
        graph[node].append(i+1)

    for i in range(node_num):
        cur_node = i+1
        dist = set()

        dist.add(cur_node)
        dfs(graph, cur_node, dist)
        dist.remove(cur_node)

    print(len(max_li))
    
    list(max_li).sort()
    for i in max_li:
        print(i)

    return


if __name__ == "__main__":
    main()


# from copy import deepcopy
# #2의 100승 = dfs? 100만개?
# # 뎁스 1000까지 가능.

# max_size = float("-inf")
# max_li = []

# #가지치기 = 같은게 두개
# def dfs(num_arr, index_set, num_set, cur_idx, max_num):
#     global max_size
#     global max_li
#     if cur_idx == max_num:
#         if index_set != num_set:
#             return
#         size = len(num_set)
#         max_size = max(max_size, size)
#         max_li = list(num_set)
#         return

#     if len(index_set) + max_num - cur_idx <= max_size:
#         # print(index_set, len(index_set) + max_num - cur_idx, max_size)
#         return

#     #숫자를 넣어야 함. index 아님.
#     #숫자를 넣으려면 현재 인덱스가 넘지 않았거나, index_set에 있으면 됨.
#     if cur_idx > num_arr[cur_idx] and num_arr[cur_idx] not in index_set:
#         pass
#     else:
#         index_set.add(cur_idx+1)
#         num_set.add(num_arr[cur_idx])
#         dfs(num_arr, index_set, num_set, cur_idx+1, max_num)
#         index_set.remove(cur_idx+1)
#         num_set.remove(num_arr[cur_idx])

#     if num_arr[cur_idx] in num_set:
#         # print("중복 선택 가지치기:", num_set, num_arr[cur_idx])
#         return
#     #선택을 안하려면 num_set에 현재 index가 없어야 함.
#     if num_arr[cur_idx] not in num_set:
#         # print("선택 안하는 DFS로:",num_set, num_arr[cur_idx])
#         dfs(num_arr, index_set, num_set, cur_idx+1, max_num)
#     # else:
#         # print("선택 안하는 DFS 가지치기:",num_set, num_arr[cur_idx])

#     return

# def main():
#     global max_size
#     global max_li
#     num = int(input())
#     num_arr = []
#     for _ in range(num):
#         num_arr.append(int(input()))

#     dfs(num_arr, set(), set(), 0, num)

#     print(max_size)
#     max_li.sort()
#     for elem in max_li:
#         print(elem)
#     return

# if __name__ == "__main__":
#     main()