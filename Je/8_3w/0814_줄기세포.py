import sys
sys.stdin = open("Je/8_3w/input.txt")


'''
문제 링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo

배양 시간 동안 아래 일을 진행한다

1. 비활성이면
- 비활성 count 감소

2. 활성이면
- 활성 count 감소 (활성 count 0되면 죽은 셀이 된다)
- 상하좌우로 번식
- 번식된거는 비활성으로 초기화
- 번식했는데 겹치면 생명력 더 높은 놈으로
'''


def make_sparse_matrix(row, col, arr_2d):
    sparse_matrix = dict()
    for i in range(row):
        for j in range(col):
            if arr_2d[i][j] == 0:  continue
            key = (i, j)  # key: 좌표값
            value = [arr_2d[i][j], arr_2d[i][j], False]  # value: [생명력 수치, 생명력 카운트(초기값은 생명력 수치와 같다), 활성 상태 체크]
            sparse_matrix[key] = value

    return sparse_matrix


def calculate_alive_cells(cells: dict):
    alive_cnt = 0
    for cell_info in cells.values():
        _, vital_cnt, active = cell_info
        
        if active and vital_cnt == 0:  # 죽은 세포는 계산 안한다
            continue

        alive_cnt += 1
    return alive_cnt


def main():
    T = int(input())
    
    for test_case in range(1, T+1):
        N, M, K = map(int, input().split())  # 세로 크기, 가로 크기, 배양 시간
        grid = [list(map(int, input().split())) for _ in range(N)]

        '''
        grid의 대부분의 값이 0으로 채워져 있음
        그리고 grid의 크기는 문제에서 무한하다 하였으므로 dictionary 기반의 sparse matrix 구조 사용

        sparse matrix 장점
        - 배열에서 값이 존재하는 위치만을 저장할 수 있으므로 대부분의 값이 0인 경우 메모리 절약 가능
        - 무한히 큰 배열에서도 필요한 부분만 다룰 수 있음

        sparse matrix 단점
        - 모든 셀에 값을 채우는 경우 리스트보다 느릴 수 있다
        '''
        cells = make_sparse_matrix(N, M, grid)

        # K 시간 동안 줄기세포 배양 진행
        while K:
            spread = {}  # 이번 턴에 번식한 놈들 저장
            for pos in cells.keys():
                x, y = pos
                vitality, vital_cnt, active = cells[pos]

                # 1. 비활성일 경우
                if not active:
                    if vital_cnt > 0:  # 생명력 수치가 남아있을 경우 -> 생명력 수치 1 감소
                        cells[pos][1] -= 1
                    if cells[pos][1] == 0:  # 활성 상태에 진입 -> 생명력 최대로 초기화
                        cells[pos] = [vitality, vitality, True]

                # 2. 활성일 경우
                else:
                    # 활성 상태 이면서 생명력 수치가 0일 경우 죽은 세포임
                    if vital_cnt == 0:  continue
                    
                    # 상하좌우로 세포 번식
                    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        new_pos = (nx, ny)

                        # 만약 이미 이전에 배양된 세포가 있으면 번식한 놈을 추가하지 않는다 (이번에 번식한 놈들에 대해서만 진행)
                        if new_pos in cells.keys():  continue
                        
                        if new_pos not in spread.keys():
                            spread[new_pos] = [vitality, vitality, False]
                        else:
                            # 생명력 비교하여 더 큰 생명력 가진 세포가 먹는다
                            if spread[new_pos][0] < vitality:
                                spread[new_pos] = [vitality, vitality, False]

                    cells[pos][1] -= 1
           
            # 새로 번식한 놈들을 추가해준다
            for new_pos, cell_info in spread.items():
                if new_pos in cells:
                    if cells[new_pos][0] < cell_info[0]:
                        cells[new_pos].append(cell_info)
                else:
                    cells[new_pos] = cell_info
            
            K -= 1  # 시간 감소
        
        result = calculate_alive_cells(cells)

        print(f"#{test_case} {result}")


if __name__ == "__main__":
    main()