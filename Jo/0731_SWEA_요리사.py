from itertools import combinations

# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    # 음식 간 시너지 table
    synergy = [list(map(int, input().split())) for _ in range(N)]

    # 시너지 인덱스 list
    idx_lst = list(range(N))

    # 시너지 간 최소 차이 값 저장
    min_diff = 987654321

    # 반으로 가르기
    a_food_combs = list(combinations(idx_lst, N//2))
    for comb in a_food_combs:
        b_food_comb = tuple([num for num in idx_lst if num not in comb])

        a_pairs = list(combinations(comb, 2))
        b_pairs = list(combinations(b_food_comb, 2))

        # A와 B 총 시너지 초기화
        a_sum = 0
        b_sum = 0

        # 각각 시너지 합 구하기
        for a_pair, b_pair in zip(a_pairs, b_pairs):
            a_sum += synergy[a_pair[0]][a_pair[1]] + synergy[a_pair[1]][a_pair[0]]
            b_sum += synergy[b_pair[0]][b_pair[1]] + synergy[b_pair[1]][b_pair[0]]

        # 절댓값을 통한 차이 구하기
        diff = abs(a_sum - b_sum)

        # 기존의 최소값보다 작을 시에 갱신
        if diff < min_diff:
            min_diff = min(diff, min_diff)

    print(f'#{test_case} {min_diff}')