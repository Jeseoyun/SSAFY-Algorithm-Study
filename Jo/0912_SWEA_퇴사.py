def dfs(n, total_money):
    global max_money

    if n>=N:
        max_money = max(max_money, total_money)
        return

    # 상담하는 경우
    if n+T[n]<=N:
        dfs(n+T[n], total_money + P[n])
    # 상담 하지 않는 경우
    dfs(n+1, total_money)

N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

max_money = 0
dfs(0, 0)
print(max_money)