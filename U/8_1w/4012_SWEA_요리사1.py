# for문 돌려서 조합 안 구하고 바로 계산하기

from itertools import combinations
import sys

# 입력 파일을 표준 입력으로 설정
sys.stdin = open('4012_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    # 식재료 수 N
    N = int(input())

    food_score = [list(map(int, input().split())) for _ in range(N)]
    food_idx = [i for i in range(N)]
    min_diff = float('inf')

    # N개 중 N//2개를 고른 조합 리스트
    half = N // 2
    comb_list = list(combinations(food_idx, half))

    for comb in comb_list:
        first_comb = list(comb)
        second_comb = [idx for idx in food_idx if idx not in first_comb]

        first_food_score = 0
        second_food_score = 0

        # 첫 번째 음식 점수 계산
        for i in range(half):
            for j in range(i + 1, half):
                first_food_score += food_score[first_comb[i]][first_comb[j]]
                first_food_score += food_score[first_comb[j]][first_comb[i]]

        # 두 번째 음식 점수 계산
        for i in range(half):
            for j in range(i + 1, half):
                second_food_score += food_score[second_comb[i]][second_comb[j]]
                second_food_score += food_score[second_comb[j]][second_comb[i]]

        min_diff = min(abs(first_food_score - second_food_score), min_diff)

    print(f"#{tc} {min_diff}")
