'''
문제에서 신경써야할 조건 정리
1. 미생물 군집이 arr 사이드에 닿으면 virus_count는 2로 나눈다, move_di의 방향은 반대로 바꿔준다
2. 미생물 수가 0이되는 집단은 사라진다
3. 이동 후 두 개 이상의 군집이 한 셀에 모이는 경우 군집들이 합쳐진다 => 생각 : 그렇다면 arr를 3중 배열을 사용해서??
메모리 오류 가능성이 너무 높다 그럼 dict를 던지자
4. 군집이 합쳐질 때 고려해야하는 것은 이동방향 이동방향은 virus_count가 가장 많은 군집의 이동방향으로

*** 핵심
x_pos, y_pos, virus_count, move_di
0      1      2           3


x, y, virus_num, virus_di는 for문 내에서 dict의 내용을 바꾸기 위해 사용하는 변수
'''

# 방향전환 알고리즘 생각한 방식
# 인덱스가 홀수인 경우 -1 인덱스가 짝수인 경우 +1하는 방식으로
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for test_case in range(1, T + 1):
    cell_count, time, virus_group_count = map(int, input().split())
    virus_info = []
    answer = 0

    # 입력 받는 구간
    for i in range(virus_group_count):
        x_pos, y_pos, virus_count, move_di = map(int, input().split())
        virus_info.append([x_pos, y_pos, virus_count, move_di - 1])

    # 시뮬레이션 시작
    for _ in range(time):
        next_arr = {}

        for i in range(len(virus_info)):
            x, y, virus_num, virus_di = virus_info[i]

            # 이동
            nx = x + dx[virus_di]
            ny = y + dy[virus_di]

            # 약품이 칠해진 셀에 도달한 경우
            if nx <= 0 or ny <= 0 or nx >= cell_count - 1 or ny >= cell_count - 1:
                virus_num //= 2
                if virus_di % 2 == 0:  # 위에서 적은대로 인덱스가 짝수인 경우 +1
                    virus_di = virus_di + 1
                else:
                    virus_di = virus_di - 1

            if virus_num > 0:  # 살아남은 미생물이 있는 경우에만
                if not next_arr.get((nx, ny)):  # 만일 next_arr에 값이 없는 경우 = 충돌이 없을 경우
                    # 마지막에 virus_num을 한번 더 쓴 이유는 다음에 들어온 객체와 충돌이 발생하였을 경우 값을 비교하여 방향을 설정하기 위해
                    next_arr[(nx, ny)] = [nx, ny, virus_num, virus_di, virus_num]
                else:
                    next_arr[(nx, ny)][2] += virus_num
                    if next_arr[(nx, ny)][4] < virus_num:
                        next_arr[(nx, ny)][3] = virus_di
                        next_arr[(nx, ny)][4] = virus_num

        virus_info = [info[:4] for info in next_arr.values()] # 슬라이싱을 통해 마지막 값을 날려주고 virus_info를 편집해줌
    
    for info in virus_info:
        answer += info[2]  

    print(f'#{test_case} {answer}')

