from collections import deque

n = int(input())
arr = list(map(int, input().split()))
tree = [[-1] for _ in range(n)]
del_n = int(input())
count = 0
root = -1

for i in range(len(arr)):
    if arr[i] != -1:
        tree[arr[i]] += [i]
    else:
        root = i

q = deque()
for i in tree[root]:
    q.append(i)

while q and del_n != root:
    cur = q.popleft()
    if cur == -1:
        continue
    if cur == del_n:
        continue
    if len(tree[cur]) == 1:
        count += 1
    else:
        for i in tree[cur]:
            if i == del_n and len(tree[cur]) == 2:
                count += 1
            q.append(i)

if count == 0 and del_n != root:
    count = 1
print(count)