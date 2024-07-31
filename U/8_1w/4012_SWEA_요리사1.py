# for문 돌려서 조합 안 구하고 바로 계산하기

from itertools import combinations
import sys

# 입력 파일을 표준 입력으로 설정
sys.stdin = open('4012_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # 식재료 수 N
    N = int(input())
    food_score = [list(map(int, input().split())) for _ in range(N)]

    food_idx = [i for i in range(N)]    # 식재료 인덱스
    min_diff = float('inf')     # 최소 차이값 저장

    ingredients_num = N//2    # 각 음식에서 사용할 수 있는 식재료의 수

    # 식재료 인덱스에서 사용할 수 있는 식재료 수만큼 선택하는 조합 생성
    A_ingredients_group = list(combinations(food_idx, ingredients_num))
    
    for A_comb in A_ingredients_group:
        # 튜플 형식 리스트로 변경
        A_ingredients_group = list(A_comb)
        # B 음식 사용 가능한 재료는 A 음식 재료 그룹에 속하지 않은 재료들
        # 전체 재료 인덱스 중 A 음식 재료 그룹에 속하지 않은 인덱스만 리스트로 반환
        B_ingredients_group = [ingredients_idx for ingredients_idx in food_idx if ingredients_idx not in A_ingredients_group]

        # 음식 점수 계산용 변수
        # 매 그룹별 점수 계산해야 하니까 for문 안에서 변수 초기화
        A_food_score = 0
        B_food_score = 0

        # A 식재료 후보 중 2개 선택한 값을 리스트로 반환
        a = [list(comb) for comb in combinations(A_ingredients_group, 2)]
        b = [list(comb) for comb in combinations(B_ingredients_group, 2)]

        print(a)

        # 점수 계산
        for pair in a:
            A_food_score += food_score[pair[0]][pair[1]] + food_score[pair[1]][pair[0]]
        for pair in b:
            B_food_score += food_score[pair[0]][pair[1]] + food_score[pair[1]][pair[0]]
        min_diff = min(min_diff, abs(A_food_score - B_food_score))

    # print(f'#{tc} {min_diff}')
