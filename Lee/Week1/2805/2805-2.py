import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 중간 인덱스
    center_num = N // 2
    # 앞쪽 인덱스 증감 숫자
    front_num = center_num
    # 뒤쪽 인덱스 증감 숫자
    back_num = center_num

    # 농작물 수확 점수 저장
    farm_score = 0

    # 배열의 모든 값 접근
    for i in range(len(arr)):
        # 중간 행까지 점수 계산
        if i <= center_num:
            for j in range(front_num, back_num + 1):
                farm_score += arr[i][j]
            # 중간값이랑 같을때 증감 실행시 Out of Index
            if i < center_num:
                front_num -= 1
                back_num += 1
        # 중간 이후 점수 계산
        if i > center_num:
            for j in range(front_num + 1, back_num):
                farm_score += arr[i][j]
            front_num += 1
            back_num -= 1

    print(f'#{test_case} {farm_score}')
