import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def comb(arr, n):
    result = []
    if n == 1:
        return [[i] for i in arr]
    else:
        for i in range(len(arr)):
            elem = arr[i]
            for rest in comb(arr[i+1:], n-1):
                result.append([elem] + rest)

    return result

score_dict = {}

for test_case in range(1, T + 1):
    num = int(input())
    food_arr = [list(map(int, input().split())) for _ in range(num)]

    #음식 선택의 경우의 수
    result = comb(range(num), num/2)
    #print(result)

    #모든 경우를 점수 계산한 dict 생성
    score_dict = {}

    for calc in result:
        if tuple(calc) in score_dict:
            continue
        score = 0
        #점수 계산
        for first in calc:
            for second in calc:
                score += food_arr[first][second]

        score_dict[tuple(calc)] = score
    #print(score_dict)


    min_point = 987654321

    for calc in result:
        # 반대 생성
        compare_arr = [x for x in range(num) if x not in calc]
        #print(calc)
        #print(compare_arr)
        min_point = min(min_point, abs(score_dict[tuple(calc)] - score_dict[tuple(compare_arr)]))

    print(f"#{test_case} {min_point}")

