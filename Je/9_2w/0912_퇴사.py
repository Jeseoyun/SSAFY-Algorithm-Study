max_revenue = 0

def dfs(idx, curr_revenue):
    global max_revenue

    # 퇴사일(N)을 넘어가는 경우 종료
    if idx >= N:
        max_revenue = max(max_revenue, curr_revenue)
        return

    # 이번 상담을 하지 않고 다음 날로 이동
    dfs(idx + 1, curr_revenue)

    # 이번 상담을 할 수 있는 경우 (퇴사일을 넘지 않는 경우)
    if idx + plan[idx][0] <= N:
        dfs(idx + plan[idx][0], curr_revenue + plan[idx][1])


N = int(input())
plan = [list(map(int, input().split())) for _ in range(N)]

dfs(0, 0)

print(max_revenue)
