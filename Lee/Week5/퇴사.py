# https://www.acmicpc.net/problem/14501

# dfs로 풀어 볼거임
def sol(index, total_amount, visited):
    global result
    
    # 현재 위치가 n보다 클때
    if index >= n:
        result = max(result, total_amount)
        return

    sol(index + 1, total_amount, visited)
    
    # 다음 값이 arr 안에 값이면 다음 값 선택
    if index + arr[index][0] <= n:
        visited[index] = 1
        sol(index + arr[index][0], total_amount + arr[index][1], visited)
        visited[index] = 0


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
visited = [0] * n
sol(0, 0, visited)

print(result)