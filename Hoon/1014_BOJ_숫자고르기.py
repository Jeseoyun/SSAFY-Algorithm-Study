from copy import deepcopy
#2의 100승 = dfs? 100만개?
# 뎁스 1000까지 가능.

max_size = float("-inf")
max_li = []

#가지치기 = 같은게 두개
def dfs(num_arr, index_set, num_set, cur_num, max_num):
    global max_size
    global max_li
    if cur_num == max_num:
        if index_set != num_set:
            return
        size = len(num_set)
        max_size = max(max_size, size)
        max_li = list(num_set)
        return

    if len(index_set) + max_num - cur_num <= max_size:
        print(index_set, len(index_set) + max_num - cur_num, max_size)
        return


    if num_arr[cur_num] in num_set:
        # print("중복 선택 가지치기:", num_set, num_arr[cur_num])
        return
    #숫자를 넣어야 함. index 아님.
    #숫자를 넣으려면 현재 인덱스가 넘지 않았거나, index_set에 있으면 됨.
    if cur_num <= num_arr[cur_num] or num_arr[cur_num] in index_set:
        index_set.add(cur_num+1)
        num_set.add(num_arr[cur_num])
        dfs(num_arr, index_set, num_set, cur_num+1, max_num)
        index_set.remove(cur_num+1)
        num_set.remove(num_arr[cur_num])

    #선택을 안하려면 num_set에 현재 index가 없어야 함.
    if num_arr[cur_num] not in num_set:
        # print("선택 안하는 DFS로:",num_set, num_arr[cur_num])
        dfs(num_arr, index_set, num_set, cur_num+1, max_num)
    # else:
        # print("선택 안하는 DFS 가지치기:",num_set, num_arr[cur_num])
    
    return

def main():
    global max_size
    global max_li
    num = int(input())
    num_arr = []
    for _ in range(num):
        num_arr.append(int(input()))

    dfs(num_arr, set(), set(), 0, num)

    print(max_size)
    max_li.sort()
    for elem in max_li:
        print(elem)
    return

if __name__ == "__main__":
    main()