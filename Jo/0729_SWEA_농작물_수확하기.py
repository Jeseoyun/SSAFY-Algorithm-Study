T = int(input())

for test_case in range(1, T + 1):
    #농장의 크기
    N = int(input())
    #농장
    farm = [input() for _ in range(N)]
    #전체 가치
    total_value = 0

    #가운데 지점
    mid = N//2

    #가운데 기준 상단
    if N >= 3:
        for i in range(mid):
            part = farm[i][mid - i: mid + i + 1]
            for num in part:
                total_value += int(num)

    #가운데
    for num in farm[mid]:
        total_value += int(num)

    #가운데 기준 하단
    if N >= 3:
        for i in range(mid):
            part = farm[mid + i + 1][i + 1: N - i - 1]
            for num in part:
                total_value += int(num)

    print(f'#{test_case} {total_value}')