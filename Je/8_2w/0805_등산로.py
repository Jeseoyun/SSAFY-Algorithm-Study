import sys
# sys.stdin = open("8_2w\등산로_error_case.txt")


'''
문제 링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq
'''

# 1. 가장 높은 봉우리에서 시작 -> 여러 개 일 수 있다
# 2. 반드시 높이가 높->낮 이동
# 3. 단 1회 최대 K만큼 지형 깎을 수 있다
# - 최소로 깎아야 갈 수 있는 지점이 조금이라도 많아짐
# - 최소로 깎는다? (nx, ny)가 (x, y)에서의 값보다 딱 1만 작게
# - 즉 (nx, ny) <= (x, y) 일 경우: (nx, ny) - (x, y) + 1


from collections import deque
import copy


def find_start_point(map, N):
    peak = 0
    peak_points = []
    
    for i in range(N):
        for j in range(N):
            if peak < map[i][j]:
                peak = map[i][j]
                peak_points = [(i, j)]
            elif peak == map[i][j]:
                peak_points += [(i, j)]
            
    return peak_points


def hiking_trail_bfs(hiking_map, N, K, start_x, start_y):
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 시작 지점 초기값 설정
    path_init = {(start_x, start_y)}
    queue = deque([(start_x, start_y, path_init, hiking_map[start_x][start_y], False)])
    # queue => (x좌표, y좌표, 지금까지 방문 경로, 현재 지점의 높이, 깎은 적이 있는지, 이동한 길이)

    max_length = 1
        
    while queue:
        # print(queue)
        x, y, path, curr_height, FLAG = queue.popleft()
        
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            # 범위 벗어난 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            # 이미 방문한 경우
            if (nx, ny) in path:
                continue
            
            # 1. 이동할 지점이 더 낮은 경우 -> 그 지점으로 바로 이동
            if hiking_map[nx][ny] < curr_height:
                new_path = copy.deepcopy(path)  # 집합은 리스트처럼 mutable -> deepcopy 해줘야함
                new_path.add((nx, ny))
                queue.append((nx, ny, new_path, hiking_map[nx][ny], FLAG))
            
            # 2. 이동할 지점이 더 높거나 같은 경우(elif 조건문 사용)
            # K만큼 깎을 수 잇는 기회 1번 있음 
            # K를 썼는지 안썼는지 알기 위해 FLAG를 두자
            # -> 이전에 K만큼 지형 깎은 적 없으면 깎고 이동
            elif not FLAG:
                if hiking_map[nx][ny] - curr_height + 1 <= K:
                    new_path = copy.deepcopy(path)
                    new_path.add((nx, ny))
                    # hiking_map[nx][ny] = hiking_map[x][y] - 1   # 일케 하면 배열 자체가 아예 바뀌어버림
                    new_height = curr_height - 1  # 현재 지점보다 1 작으면 최소로 깎는거시다
                    queue.append((nx, ny, new_path, new_height, True))

            max_length = max(max_length, len(new_path))

    return max_length


def main():
    T = int(input())
    
    for test_case in range(1, T+1):
        N, K = map(int, input().split())
        hiking_map = [list(map(int, input().split())) for _ in range(N)]
        
        # 1. 가장 높은 지점 찾기
        start_points = find_start_point(hiking_map, N)
        
        # 2. bfs 순회
        root_length = []
        for start_x, start_y in start_points:
            root_length.append(hiking_trail_bfs(hiking_map, N, K, start_x, start_y))
        
        result = max(root_length)
        print(f"#{test_case} {result}")


if __name__ == "__main__":
    main()