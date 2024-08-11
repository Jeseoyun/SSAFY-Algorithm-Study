import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, B = list(map(int, input().split()))
    H = list(map(int, input().split()))

    min_diff = 987654321

    def dfs(arr, idx):
        global min_diff

        #기존의 최소 높이차가 (점원들 키의 합 - 탑의 높이) 보다 작다면 싹둑 
        if min_diff < sum(arr) - B:
            return
        # 배열의 끝까지 다 순회했을 때 
        if idx == N:
            # 배열의 합이 B보다 크다면
            if sum(arr) >= B:
                # 기존의 최소 높이차보다 작다면 갱신
                min_diff = min(min_diff, sum(arr) - B)
            return
        
        #해당 원소를 포함할 경우
        dfs(arr + [H[idx]], idx + 1)
        # 해당 원소를 포함하지 않을 경우
        dfs(arr, idx + 1)

    dfs([], 0)

    print(f'#{test_case} {min_diff}')
