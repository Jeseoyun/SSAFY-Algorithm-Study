from collections import deque

import sys
sys.stdin = open('input.txt')

#상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

#방향 뒤집는 인덱스
reverse = [1, 0, 3, 2]

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        size, max_time, num = map(int, input().split())

        q = deque([])

        for _ in range(num):
            y, x, cnt, cur_dir = map(int, input().split())
            #숫자, 방향
            q.append((y, x, cur_dir - 1, cnt))

        #시간동안 돌기
        for _ in range(max_time):

            visited = {}
            while q:
                y, x, cur_dir, cur_cnt = q.popleft()

                ny = y + dy[cur_dir]
                nx = x + dx[cur_dir]

                #약품 구역에서 합쳐질수는 없음.
                if ny == 0 or nx == 0 or ny == size-1 or nx == size-1:
                    visited[(ny, nx)] = [(reverse[cur_dir], int(cur_cnt/2))]
                    continue
                
                #합쳐짐 판단
                #판단은 유보함
                if (ny, nx) in visited.keys():
                    visited[(ny, nx)].append((cur_dir, cur_cnt))

                else:
                    visited[(ny, nx)] = [(cur_dir, cur_cnt)]

            #다음 큐 만들기
            #여기서 방향 판단
            for key, value in visited.items():
                max_cnt = float('-inf')
                cur_dir = -1
                cur_cnt = 0
                if len(value) == 1:
                    cur_dir = value[0][0]
                    cur_cnt = value[0][1]
                else:
                    for elem in value:
                        cur_cnt += elem[1]
                        if max_cnt < elem[1]:
                            max_cnt = elem[1]
                            cur_dir = elem[0]


                q.append((key[0], key[1], cur_dir, cur_cnt))

        sum = 0
        #print(visited.items())
        for value in q:
            sum += value[3]

        print(f"#{test_case} {sum}")

if __name__ == "__main__":
    main()