# dfs가 너무 싫어요....
# 로직은 먼저 4중 for문으로 앞의 2중 for문에서 한칸씩 전진합니다
# 문제 예시 였던 아래 arr로 설명하자면
# 4 2 13
# 6 1 9 7
# 9 8 5 8
# 3 4 5 3
# 8 2 6 7
# (6,1)의 숫자로 만들 수 있는 합이 c를 넘지 않으며 서로 제곱했을 때의 합 최대값을 찾습니다.
# 뒤의 2중 for문은 그렇게 찾은 값 뒤의 배열을 하나 하나 다 검색하며 최대값을 찾습니다
# 로직 정말 별로입니다...
# 그래서 (6,1)에서 나올 수 있는 최대값인 37을 저장하고 뒤의 for문은 (0,0)(0,1) 다음의 arr은 다 검사합니다
# 그렇게 4중 for문을 돌고 다시 처음으로 오면 이제 (1,9)를 이용합니다. 그 후 또 arr 전체를 돕니다. 숫자가 커지면 동작시간이 정말 커질 것으로 예상합니다

def dfs(idx, honey_benefit, honey_sum, x, y, arr, M, C):
    global part_sum
    if honey_sum > C:
        return

    if idx == M:
        part_sum = max(part_sum, honey_benefit)
        return

    current_benefit = arr[x][y + idx] ** 2
    current_sum = arr[x][y + idx]

    # 현재 꿀을 선택하거나
    dfs(idx + 1, honey_benefit + current_benefit, honey_sum + current_sum, x, y, arr, M, C)
    # 현재 꿀을 선택하지 않거나
    dfs(idx + 1, honey_benefit, honey_sum, x, y, arr, M, C)

T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0

    for fst_i in range(N):
        for fst_j in range(N - M + 1):
            part_sum = 0
            dfs(0, 0, 0, fst_i, fst_j, arr, M, C)
            fst_max = part_sum

            for snd_i in range(fst_i, N):
                for snd_j in range(0, N - M + 1):
                    if fst_i == snd_i and snd_j < fst_j + M:
                        continue
                    part_sum = 0
                    dfs(0, 0, 0, snd_i, snd_j, arr, M, C)
                    snd_max = part_sum
                    max_sum = max(max_sum, fst_max + snd_max)

    print(f"#{test_case} {max_sum}")
