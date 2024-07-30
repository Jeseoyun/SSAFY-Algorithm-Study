'''
문제링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH
'''

import sys
sys.stdin = open("Je/input.txt")


def half_split(arr, comb, idx, result):
    if len(comb) == len(arr)//2:
        result.append(comb[:])
    
    for i in range(idx, len(arr)):
        comb.append(arr[i])
        half_split(arr, comb, i+1, result)
        comb.pop()


def min_taste_diff(synergy, N):
    # N개의 재료를 N//2개로 나눈다
    food_half_split = []
    half_split(range(N), [], 0, food_half_split)
    
    # 한 번 선택한 재료는 다시 사용하지 못함
    # 이를 고려해서 음식 A / 음식 B 나누기
    food_comb = []
    for idx_a, food_a in enumerate(food_half_split):
        for food_b in food_half_split[idx_a:]:
            # 두 개의 리스트 중 겹치는 원소가 하나도 없는 경우만 찾기
            # -> 집합으로 변환하여 교집합이 비어있으면 추가
            if set(food_a).isdisjoint(set(food_b)):
                food_comb.append([food_a, food_b])

    min_synergy = float('inf')
    
    for a_ing, b_ing in food_comb:
        food_a = synergy[a_ing[0]][a_ing[1]] + synergy[a_ing[1]][a_ing[0]]
        food_b = synergy[b_ing[0]][b_ing[1]] + synergy[b_ing[1]][b_ing[0]]
        
        min_synergy = min(min_synergy, abs(food_a-food_b))
        
    return min_synergy


def main():
    T = int(input())
    
    for test_case in range(1, T+1):
        N = int(input())
        synergy = [list(map(int, input().split())) for _ in range(N)]
        
        result = min_taste_diff(synergy, N)
        
        print(f"#{test_case} {result}")



if __name__ == "__main__":
    main()