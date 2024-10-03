CNT = 5
is_true = 0

def dfs(graph, node, friend_cnt, visited):
    global is_true
    if friend_cnt == 5:
        is_true = 1
        return
    
    for next_node in graph[node]:
        if visited[next_node] == 1:
            continue
        visited[next_node] = 1
        dfs(graph, next_node, friend_cnt + 1, visited)
        visited[next_node] = 0

    return

def main():
    global is_true
    node_num, edge_num = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(edge_num)]
    visited = [0] * node_num

    graph = {}
    
    for i in range(node_num):
        graph[i] = []

    # print(graph)

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    for i in range(node_num):
        visited[i] = 1
        dfs(graph, i, 1, visited)
        visited[i] = 0
        
        if is_true == 1:
            break
    
    print(is_true)

    return

if __name__ == "__main__":
    main()