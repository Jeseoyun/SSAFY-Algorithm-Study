# DFS
def dfs(idx,sub_word):
    global cnt
    if idx==N:
        if len(set(sub_word))==26: cnt+=1
        return
    dfs(idx+1,sub_word+arr[idx])
    dfs(idx+1,sub_word)


# main
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(input().strip()) for _ in range(N)]
    cnt=0
    dfs(0,[])
    print(f'#{tc}',cnt)

