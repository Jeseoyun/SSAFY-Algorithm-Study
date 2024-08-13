import heapq

import sys
sys.stdin = open('input.txt')

# 배우게 된 발상
#1. BFS처럼 q로 처리하되, q에 담긴 정보들을 처리해야하는 경우 for문으로 한단계씩 검사하기
#2. q를 우선순위 q로 처리하는 경우, BFS 처럼 한단계씩 탐색을 진행하되, 그 중에서도 우선순위를 줄 수 있음

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        size_y, size_x, time = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(size_y)]

        max_heap_active = []

        is_arrived = set()

        #시작 넣어주기
        for y in range(size_y):
            for x in range(size_x):
                #max_heap
                #기본이 min_heap
                if board[y][x] != 0:
                    # 생명력(음수), y좌표, x좌표, 활성화를 위해 기다린 시간
                    heapq.heappush(max_heap_active, (-board[y][x], y, x, 0))
                    is_arrived.add((y, x))

        #시간만큼 돌아가는 for문
        for cur_time in range(time):
            #다음 타임의 queue를 준비하되, max_heap_active에 다시 넣지 않으면 시간마다 분리 가능.
            next_queue  = []
            while max_heap_active:
                temp_hp, y, x, waiting_time = heapq.heappop(max_heap_active)
                temp_hp = -temp_hp
                
                #활성화가 안 되었다면,
                if temp_hp > waiting_time:
                    heapq.heappush(next_queue, (-temp_hp, y, x, waiting_time+1))
                    continue

                # 살아있는 코드를 세야함.
                if waiting_time + 1 < temp_hp * 2:
                    heapq.heappush(next_queue, (-temp_hp, y, x, waiting_time+1))

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    #있으면 생명력이 쌘 애임
                    if (ny, nx) in is_arrived:
                        continue

                    heapq.heappush(next_queue, (-temp_hp, ny, nx, 0))
                    is_arrived.add((ny, nx))

            max_heap_active = next_queue.copy()
        #print(is_arrived)

        print(f"#{test_case} {len(max_heap_active)}")

if __name__ == "__main__":
    main()