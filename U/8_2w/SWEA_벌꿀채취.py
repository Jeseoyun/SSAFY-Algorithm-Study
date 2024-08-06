'''
8/3
dfs로 풀어야할 거 같은데
감이 안 잡히네 이거 어캄?

8/4 
벌통 지정.
해당 벌통 꿀양 조합을 구함
조합의 합이 최대 수확량(C)를 넘지 않으면서 가장 큰 값을 찾음 => 가지치기

'''

from itertools import combinations
import sys
sys.stdin = open('honey_input.txt', 'r')

T = int(input())


# 부분 집합의 합을 구하고 최대 수익 값을 찾는 dfs
# 합이 C보다 큰 경우 수익을 구하지 않고 다음으로 넘어간다. => 가지치기
def search(idx, honey_income, comb_sum, y, x):
    global comb_income

    # 가지치기
    if comb_sum > C:
        return
    
    # 종료 조건 : M개의 꿀통의 선택 여부를 전부 결정함
    if idx == M:
        comb_income = max(comb_income, honey_income)
        return

    # 해당 인덱스의 꿀통을 선택한 경우
    # 다음 선택 인덱스를 넘겨줌 (idx+1)
    # 현재 벌꿀 수익에 해당 좌표의 수익 더해서 넘김
    # 벌꿀 값도 더해서 넘김
    # y는 그대로 x인덱스는 1 증가해서 넘김
    # 두 번째 의문 // 지점 뭐가 다른겨 ......
    # 좌표를 옮겨주는 아래 코드(내 코드) 보다는 좌표는 변경하지 않는 선생님 방식이 더 좋대
    search(idx+1, honey_income+honey_board[y][x]**2,comb_sum+honey_board[y][x], y, x+1)
    # search(idx+1, honey_income+honey_board[y][x+idx]**2,comb_sum+honey_board[y][x+idx], y, x)
    # 해당 인덱스의 꿀통을 선택하지 않은 경우
    search(idx+1, honey_income, comb_sum, y, x+1)

    

for tc in range(1, T+1):
    # 벌통의 크기 N / 선택할 수 있는 벌통 수 M / 꿀을 채취할 수 있는 최대 양 C
    BOARD_SIZE, M, C = map(int, input().split())
    honey_board = [list(map(int, input().split())) for _ in range(BOARD_SIZE)]
    # print(N, M, C, honey_board)
    max_honey_income = -1   # 벌꿀 최대 수익
    
    # 여기가 넘 어려운 거 같음
    # 지능 140 이상을 요함
    # a일꾼 최대 수익구하는 for문
    for a_y in range(BOARD_SIZE):
        for a_x in range(BOARD_SIZE-M+1):
            comb_income = 0    # dfs를 통해 얻은 최대 수익, dfs에서 직접 접근해서 갱신

            # 파라미터 감 1도 안 옴
            # 중단 조건 : 선택한 꿀통 수 = 선택을 진행한 idx가 M일 때 중단
            # 누적할 값 : 벌꿀 수익
            # 흠.. 꿀통 좌표
            # 조합의 합
            search(0, 0, 0, a_y, a_x)
            a_worker_max_income = comb_income

            # b일꾼의 경우 a일꾼이 고른 곳 이후의 꿀통만 골라도 됨
            # a일꾼의 y좌표부터 시작해서 행을 모두 순회함
            for b_y in range(a_y, BOARD_SIZE):
                for b_x in range(0, BOARD_SIZE-M+1):
                    # 같은 라인일 때 b일꾼의 꿀통이 a일꾼보다 앞에 있는 경우
                    # 해당 좌표의 조합을 구할 필요가 없음(이미 a가 골라서 조합해봤기 때문)
                    if a_y == b_y and a_x + M > b_x : continue  # 이거 이해 안 감..? 또잉?
                    # if a_y == b_y and a_x >= b_x + M : continue   # 처리를 못 하는 케이스가 있음
                    comb_income = 0
                    search(0, 0, 0, b_y, b_x)
                    b_worker_max_income = comb_income

                    # 기존 구했던 최대 벌꿀 수익보다 현재 구한 총 수익이 높으면 갱신
                    max_honey_income = max(max_honey_income, a_worker_max_income + b_worker_max_income)

    print(f'#{tc} {max_honey_income}')

