def dfs(node):
    tree[node] = 51
    for i in range(N):
        # 삭제할 노드를 부모로 갖는 노드가 있다면 똑같이 처리
        if node == tree[i]:
            dfs(i)

# 노드의 개수
N = int(input())
# 트리
tree = list(map(int, input().split()))
# 삭제할 노드 번호
del_node = int(input())

dfs(del_node)

cnt = 0
for i in range(N):
    # 삭제된 노드가 아니고 부모가 없다면 (리프 노드에 해당한다면)
    if tree[i] != 51 and i not in tree:
        cnt += 1

print(cnt)