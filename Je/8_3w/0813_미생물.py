import sys
sys.stdin = open("Je/8_3w/input.txt")


'''
문제 링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl

원자 소멸 시뮬레이션이랑 비슷한듯

1. 먼저 미생물을 이동방향으로 이동시킴

2. 만약 이동 후 약품 셀에 도착했을 경우
- 미생물 절반으로 줄이고 이동방향 반대로 바꿈
- 절반 줄일 때 소숫점 이하 버림

3. 만약 이동 후 두 개 이상의 군집이 모였을 경우
- 해당 지점의 미생물 모두 합침
- 이동 방향은 미생물 가장 많았던 놈의 이동방향 가져옴
'''


def find_opposite_direction(direction):
    # 상: 1 하: 2 좌: 3 우: 4
    if direction % 2:
        return direction + 1  # 홀수이면 1 더해주고
    else:
        return direction - 1  # 짝수이면 1 빼주면 방향이 바뀐다


def move(pos, direction):
    dxy = {
        1: (-1, 0), 
        2: (1, 0), 
        3: (0, -1), 
        4: (0, 1)
    }

    nx = pos[0] + dxy[direction][0]
    ny = pos[1] + dxy[direction][1]

    return (nx, ny)


def calculate_remainings(microbe):
    m_sum = 0
    for pos in microbe.keys():
        for m_li in microbe[pos]:
            m_sum += m_li[0]
    return m_sum


def main():
    T = int(input())

    for test_case in range(1, T+1):
        N, M, K = map(int, input().split())  # 셀 개수, 격리 시간, 미생물 군집 수

        microbe = {}
        for _ in range(K):
            *pos, m_num, direction = map(int, input().split())  # 세로 위치, 가로 위치, 미생물 수, 이동 방향
            
            pos = tuple(pos)  # 딕셔너리 키는 immutable 해야함
            if pos not in microbe.keys():
                microbe[pos] = []
            microbe[pos].append([m_num, direction])  # {(좌표) : [미생물 수, 이동 방향], ...}
        
        while M:
            # 1. 미생물 이동
            new_microbe = {}
            for pos in microbe.keys():
                for idx, val in enumerate(microbe[pos]):
                    new_pos = move(pos, val[1])
                    if new_pos not in new_microbe.keys():
                        new_microbe[new_pos] = []
                    new_microbe[new_pos].append(microbe[pos][idx])
            microbe = new_microbe

            for pos in microbe.keys():
                # 2. 두 개 이상 군집 모였을 경우
                if len(microbe[pos]) > 1:
                    m_sum, max_val, new_direction = 0, 0, 0  # 미생물 수의 합, 가장 많은 미생물이 몇 개 였는지, 그 때의 방향은 어디쪽이었는지
                    for idx, val in enumerate(microbe[pos]):
                        m_sum += val[0]
                        if max_val < val[0]:
                            max_val = val[0]
                            new_direction = val[1]

                    microbe[pos] = [[m_sum, new_direction]]

                # 3. 약품 셀일 경우
                if pos[0] == 0 or pos[0] == N-1 or pos[1] == 0 or pos[1] == N-1:
                    for idx, val in enumerate(microbe[pos]):
                        microbe[pos][idx][0] = int(val[0] / 2)  # 미생물 절반 줄이기
                        microbe[pos][idx][1] = find_opposite_direction(val[1])  # 이동방향 반대
                    
            M -= 1  # 시간 감소

        result = calculate_remainings(microbe)

        print(f"#{test_case} {result}")


if __name__ == "__main__":
    main()