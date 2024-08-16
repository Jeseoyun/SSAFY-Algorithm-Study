def dfs(k, hei_sum):
    global answer

# 가지치기
    # 먼저 B보다 sum이 더 큰 경우 answer값 최신화
    if hei_sum >= B:
        answer = min(hei_sum, answer)
        return
    # k가 N보다 작을 경우 == arr에 더 돌 값이 남아 있을 경우
    if k < N:
        remaining_sum = sum(arr[k:])        # 남아 있는 값들의 전체 합
    else:
        remaining_sum = 0                   # arr에 더 돌 값이 남지 않은 경우 남은 합은 0

    if hei_sum + remaining_sum < B:         # 지금까지 들어온 값과 남은 합이 B보다 작은 경우 굳이 더 돌지 않고 끝내버린다
        return

    for i in range(k, N):                   # 흔한 DFS 코드
        if not isUsed[i]:
            isUsed[i] = True
            dfs(i + 1, hei_sum + arr[i])
            isUsed[i] = False


T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    arr = sorted(map(int, input().split()), reverse=True)  # B에 가까운 값을 빠르게 찾기 위해 역순 배열
    isUsed = [False] * N
    answer = float('inf')

    dfs(0, 0)

    print(f'#{test_case} {answer - B}')
