cnt = 0

def DFS(tree, cur_node):
    global cnt

    #print(cur_node)

    if len(tree[cur_node]) == 0:
        cnt += 1
        return
    
    for child in tree[cur_node]:
        DFS(tree, child)
    
    return

def main():
    global cnt
    num = int(input())
    node_info = list(map(int, input().split()))
    del_node = int(input())

    node_info[del_node] = -2

    #print(node_info)

    tree = [[] for _ in range(num)]

    for i in range(num):
        p_node = node_info[i]
        
        if p_node == -1:
            continue

        if p_node == -2:
            continue
        
        tree[p_node].append(i)



    for i in range(num):
        if node_info[i] == -1:
            DFS(tree, i)
            break

    print(cnt)

if __name__ == "__main__":
    main()