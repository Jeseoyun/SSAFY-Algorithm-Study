'''
문제링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD
난이도: D4
'''


from collections import deque


T = 10  # test case 개수
MATRIX_SIZE = 16  # 입력 행렬의 크기


def find_path_bfs(maze, start_point):
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 현재 노드로부터 이동 가능한 지점: 우, 하, 좌, 상
    visited = set()  # 이미 방문한 경로 저장
    queue = deque([start_point])  # 방문할 인접 노드(상하좌우 방향) 저장
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            
            # 탐색 범위를 벗어난 경우
            if nx < 0 or nx >= MATRIX_SIZE or ny < 0 or ny >= MATRIX_SIZE:
                continue
            
            # 이미 방문한 경우
            if (nx, ny) in visited:  # 집합을 사용하면 O(1)
                continue
            
            # 벽(1)을 만났을 경우
            if maze[nx][ny] == 1:
                continue
            
            # 도착 지점(3)에 도달했을 경우
            if maze[nx][ny] == 3:
                return 1
            
            visited.add((nx, ny))  # 방문 경로에 추가
            queue.append((nx, ny))  # 다음에 방문할 경로에 추가
            
    return 0  # 도착 지점에 도달할 수 없을 경우


def find_path_dfs():
    pass


def find_start_point(maze):
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            if maze[i][j] == 2:
                return (i, j)  # 조건을 충족하는 좌표를 찾으면 return하여 불필요한 반복 제거
    return None


def main():
    for _ in range(T):
        test_case = int(input())  # test case 번호
        maze = [list(map(int, input())) for _ in range(MATRIX_SIZE)]
        
        # 출발점 찾기: (i, j)가 2인 곳이 출발점
        if not start_point:  # start_poitn가 None일 경우에 대한 예외처리
            raise("시작 지점이 설정되지 않음") 
        start_point = find_start_point(maze)

        # 출발점부터 미로 탐색
        result = find_path_bfs(maze, start_point)
        # result = find_path_dfs()
        
        print(f"#{test_case} {result}")


if __name__ == "__main__":
    main()