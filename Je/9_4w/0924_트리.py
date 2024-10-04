def dfs(curr_node):
    if curr_node not in tree.keys():
        return

    for child in tree[curr_node]:
        dfs(child)

    # 노드 삭제
    del tree[curr_node]
    removed_node.append(curr_node)


N = int(input())
parents = list(map(int, input().split()))
remove_node = int(input())

tree = {n: [] for n in range(N)}
for node, parent in enumerate(parents):
    if parent == -1:
        continue
    tree[parent].append(node)

removed_node = []
dfs(remove_node)

# 삭제된 노드를 자식으로 가지고 있는 경우 노드 삭제
for parent in tree.keys():
    for node in tree[parent]:
        if node in removed_node:
            tree[parent].remove(node)

leaf_node = 0
for parent in tree.keys():
    if not tree[parent]:
        leaf_node += 1

print(leaf_node)
