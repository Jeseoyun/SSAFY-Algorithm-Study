def back(day, cost):
    global answer
    if day > n:
        answer = max(answer, cost)
        return
    if day + arr[day][0] <= n + 1:
        back(day + arr[day][0], cost + arr[day][1])
    back(day+1, cost)


n = int(input())
arr = [0] * (n + 1)
for i in range(1, n+1):
    a, b = map(int, input().split())
    arr[i] = (a, b)

answer = 0
back(1, 0)

print(answer)
