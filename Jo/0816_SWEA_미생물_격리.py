'''
리스트 순회를 할 때 remove() 함수를 써버리면?

lst = ['a','b','c','d','e']
for i in lst:
    print(i)
    if i == 'a':
        lst.remove('a')

a
c
d
e

'''

'''

문제를 풀 때 포인트는 두 가지

1) 약품이 발라진 셀에 도착했을 때 방향 처리와 미생물 수 처리

2) 여러 미생물 군집이 모일 때 어떻게 처리할 것인지

'''


T = int(input())

for test_case in range(1, T + 1):
    N, M, K = list(map(int, input().split()))
    # 모든 미생물 row, col, 수, 방향에 대한 정보
    micro_organisms = [list(map(int, input().split())) for _ in range(K)]

    answer = 0

    # 의미 없는 방향과 상, 하, 좌, 우 (상이 1부터 시작하니까)
    dxy = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

    # 격리 시간 동안 일단 이동
    for i in range(M):
        # 삭제해야하는 애들은 따로 모으기 위한 변수
        remove_list = []
        for micro_organism in micro_organisms:
            # 방향이 상일 경우
            if micro_organism[3] == 1:
                micro_organism[0] += dxy[1][0]
                micro_organism[1] += dxy[1][1]
            # 방향이 하일 경우
            elif micro_organism[3] == 2:
                micro_organism[0] += dxy[2][0]
                micro_organism[1] += dxy[2][1]
            # 방향이 좌일 경우
            elif micro_organism[3] == 3:
                micro_organism[0] += dxy[3][0]
                micro_organism[1] += dxy[3][1]
            # 방향이 우일 경우
            else:
                micro_organism[0] += dxy[4][0]
                micro_organism[1] += dxy[4][1]

            # 약품이 칠해진 셀에 도착할 경우 방향 전환
            if micro_organism[0] == 0 or micro_organism[0] == N - 1 or micro_organism[1] == 0 or micro_organism[
                1] == N - 1:
                if micro_organism[3] == 1:
                    micro_organism[3] = 2
                elif micro_organism[3] == 2:
                    micro_organism[3] = 1
                elif micro_organism[3] == 3:
                    micro_organism[3] = 4
                else:
                    micro_organism[3] = 3

                # 약품이 칠해진 셀에 도착할 경우 미생물 수를 반타작해줌. 미생물 수 가 0이 될 경우 미생물 리스트에서 제거
                micro_organism[2] = (micro_organism[2] // 2)
                if micro_organism[2] == 0:
                    remove_list.append(micro_organism)
        for remove_item in remove_list:
            micro_organisms.remove(remove_item)

        # 합쳐질 경우 총합을 구하고 방향은 미생물 수가 가장 많은 셀의 방향으로 정한다
        # 미생물 수를 저장할 cells 먼저 생성
        cells = [[[] for _ in range(N)] for _ in range(N)]
        # cells 각 좌표에 도달한 [row, col, 미생물 수, 방향]을 추가
        for micro_organism in micro_organisms:
            cells[micro_organism[0]][micro_organism[1]].append(micro_organism)
        # cells 내에 군집이 2개 이상일 경우
        for j in range(N):
            for k in range(N):
                if len(cells[j][k]) > 1:
                    # 미생물 수를 기준으로 정렬
                    cells[j][k] = sorted(cells[j][k], key=lambda x: x[2])
                    # 방향을 최대 미생물 수를 가진 셀의 방향으로 설정
                    direction = cells[j][k][-1][3]
                    # 해당 셀에서의 미생물 수 합침
                    num = 0
                    for cell in cells[j][k]:
                        num += cell[2]
                    # 미생물 수가 합쳐지고 셀의 방향이 정해진 임시 값 생성
                    temp = [j, k, num, direction]
                    # 셀에 도달한 기존 값들 다 날려줌
                    micro_organisms = [x for x in micro_organisms if x not in cells[j][k]]
                    # 미생물 집합에 임시값 추가함
                    micro_organisms.append(temp)

    # 격리 시간이 끝나고 미생물의 값을 더해줌
    for micro_organism in micro_organisms:
        answer += micro_organism[2]

    print(f'#{test_case} {answer}')