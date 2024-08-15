import sys
sys.stdin = open("Je/8_3w/input.txt")


# 배양 시간 동안 아래 일을 진행한다

# 1. 비활성이면
# - 비활성 count 감소

# 2. 활성이면
# - 활성 count 감소 (활성 count 0되면 죽은 셀이 된다)
# - 상하좌우로 번식
# - 번식된거는 비활성으로 초기화
# - 번식했는데 겹치면 생명력 더 높은 놈으로


import heapq
import copy


def main():
    T = int(input())
    
    for test_case in range(1, T+1):
        N, M, K = map(int, input().split())  # 세로 크기, 가로 크기, 배양 시간
        grid = [list(map(int, input().split())) for _ in range(N)]

        cells = dict()
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:  continue
                # (x좌표, y좌표): [[생명력 수치, 생명력 카운트, 활성 상태 체크], [생명력 수치, 활성 상태 체크]]
                cells[(i, j)] = [grid[i][j], grid[i][j], False]
        time = 0
        while K:
            # print(f"=============== {time}시간 후, {cells} ===============")
            spread = {}  # 새로운 세포 번식을 기록할 딕셔너리
            for pos in list(cells.keys()):
                # print(pos, cells[pos])
                x, y = pos
                vitality, vital_cnt, active = cells[pos]

                # 1. 비활성일 경우
                if not active:
                    if vital_cnt > 0:
                        cells[pos][1] -= 1
                        # print(f"비활성 | 생명력 감소 | 원래 생명력: {vitality} | 남은 생명력: {cells[pos][0]}")
                    if cells[pos][1] == 0:
                        cells[pos] = [vitality, vitality, True]  # 생명력 최대로 초기화
                        # print(f"비활성 | 활성 상태 전환 | 바뀐 값: {cells[pos]}")

                # 2. 활성일 경우
                else:
                    if vital_cnt == 0:
                        # print(f"활성 | 죽은 셀")
                        continue
                    
                    # 상하좌우로 세포 번식
                    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        new_pos = (nx, ny)

                        if new_pos not in cells:
                            if new_pos not in spread:
                                spread[new_pos] = [vitality, vitality, False]
                            else:
                                # 생명력 비교하여 더 큰 생명력 가진 세포가 우선한다
                                if spread[new_pos][0] < vitality:
                                    spread[new_pos] = [vitality, vitality, False]
                            # print(f"활성 | 번식 | ({dx}, {dy}) 방향 | 번식 좌표: {new_pos} | {spread[new_pos]}")

                    cells[pos][1] -= 1
                    # print(f"활성 | 생명력 감소 | 원래 생명력: {vitality} | 남은 생명력: {cells[pos][0]}")

            # spread 딕셔너리에 기록된 새로운 세포를 cells에 추가
            for new_pos, cell_info in spread.items():
                if new_pos in cells:
                    if cells[new_pos][0] < cell_info[0]:
                        cells[new_pos].append(cell_info)
                else:
                    cells[new_pos] = cell_info
            # print("바뀐 셀: ", cells)
            K -= 1  # 시간 감소
            time += 1
        
        result = 0
        for pos, cell_info in cells.items():
            vitality, vital_cnt, active = cell_info
            # 활성 상태인 세포 개수 계산 (죽은 세포는 계산 안한다)
            if active and vital_cnt == 0:
                continue
            result += 1

        print(f"#{test_case} {result}")


if __name__ == "__main__":
    main()