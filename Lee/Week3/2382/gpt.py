import pprint
import sys
sys.stdin = open('sample_input.txt', 'r')

# 방향 설정 (상: 1, 하: 2, 좌: 3, 우: 4)
dxy = [[], [-1, 0], [1, 0], [0, -1], [0, 1]]

def move_turn(move):
    if move == 1:
        return 2
    elif move == 2:
        return 1
    elif move == 3:
        return 4
    elif move == 4:
        return 3

def simulate(N, M, K, arr):
    misangmool = {}

    for a in arr:
        x, y, k, move = a
        misangmool[(x, y)] = [(k, move)]

    for _ in range(M):
        new_misangmool = {}

        for (x, y), values in misangmool.items():
            for (k, move) in values:
                nx, ny = x + dxy[move][0], y + dxy[move][1]

                # 약품 구역에 도착한 경우
                if nx == 0 or ny == 0 or nx == N - 1 or ny == N - 1:
                    k //= 2
                    move = move_turn(move)
                    if k == 0:
                        continue

                if (nx, ny) not in new_misangmool:
                    new_misangmool[(nx, ny)] = [(k, move)]
                else:
                    new_misangmool[(nx, ny)].append((k, move))

        # 중복된 위치에 대해 처리
        for (nx, ny), values in new_misangmool.items():
            if len(values) > 1:
                total_k = sum(v[0] for v in values)
                max_k, max_move = max(values, key=lambda x: x[0])
                new_misangmool[(nx, ny)] = [(total_k, max_move)]
            else:
                new_misangmool[(nx, ny)] = values

        misangmool = new_misangmool
        # pprint.pprint(misangmool)

    result = sum(k for values in misangmool.values() for k, _ in values)
    return result

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]
    result = simulate(N, M, K, arr)
    print(f"#{test_case} {result}")
