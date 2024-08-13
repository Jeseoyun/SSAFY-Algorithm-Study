# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def dfs(idx, height_sum):
    global result

    # 현재 탑의 높이가 B보다 이상이면서, 최소값을 가질때
    if height_sum >= B:
        result = min(result, height_sum)
        return
    
    # 배열의 끝일때
    if idx == N:
        return
    
    # 현재 idx 선택
    dfs(idx + 1, height_sum + arr[idx])

    # 현재 idx 선택 X
    dfs(idx + 1, height_sum)



for test_case in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    result = float('inf')

    dfs(0, 0)
    print(f'#{test_case} {result - B}')