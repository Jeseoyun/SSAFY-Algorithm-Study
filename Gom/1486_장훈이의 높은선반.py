# DFS
def dfs(idx,sum_H):
    global ans
    if sum_H>=H:
        ans=min(sum_H-H,ans)
        return
    if idx==N: return
    dfs(idx+1,sum_H+arr[idx])
    dfs(idx+1,sum_H)

# main
T=int(input())
for tc in range(1,T+1):
    N,H=map(int,input().split())
    arr=list(map(int,input().split()))
    ans=1e9
    dfs(0,0)
    print(f'#{tc}',ans)
