import sys
sys.stdin = open("Je\8_4w\input.txt")


'''
문제 링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu

~ 문제의 조건 ~
1. 대각선 방향으로 이동, 사각형 모양을 그리며 출발지로 되돌아와야 함
- (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)
- 사각형 모양 -> 원래 가던 방향대로 가거나 / 이전에 안 가본 방향으로

2. 이동 경로에서 동일한 값을 가진게 있으면 안됨
- 경로 기록이 필요하다 -> dfs

3. 경로가 하나밖에 없거나 왔던 길을 고대로 되돌아가면 안됨

4. 디저트를 가장 많이 먹을 수 있는 경우의 개수를 구하자
'''


dxy = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
max_dessert = -1
prev = ()


def log(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()
    print("max_dessert", max_dessert)
    print()


def dfs(arr, matrix_size, start, x, y, visited, used_direction, history):
    global max_dessert, prev
    log(visited)
    
    # 1. 원래 가던 방향대로
    if prev:
        nx, ny = x + prev[0], y + prev[1]
        print((x, y),"->",(nx, ny))
    
    # 2. 새로운 방향으로
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        print((x, y),"->",(nx, ny))
        
        # 배열 크기 벗어난 경우
        if nx < 0 or nx >= matrix_size or ny < 0 or ny >= matrix_size:
            continue
        
        # 이미 방문한 경우
        if visited[nx][ny]:
            continue
        
        # 이전에 먹은 디저트 개수와 같을 경우
        if arr[nx][ny] in history:
            continue
        
        # 이전 방향은 사용 불가
        if prev and (dx, dy) not in used_direction:
            continue
        
        # 탈출 조건: 시작 지점에 다시 도착한 경우
        if (nx, ny) == start:
            max_dessert = max(max_dessert, visited[x][y] + arr[nx][ny])
            return
        
        visited[nx][ny] = visited[x][y] + arr[nx][ny]
        used_direction.append((dx, dy))
        history.add(arr[nx][ny])
        
        dfs(arr, matrix_size, start, nx, ny, visited, used_direction)
        


def cafe_tour(cafes, matrix_size):
    global max_dessert
    max_dessert = -1
    
    # 모든 점이 출발점이 될 수 있다
    for i in range(matrix_size):
        for j in range(matrix_size):
            start = (i, j)
            print(f"=========== start: {start} ===========")
            visited = [[0]*matrix_size for _ in range(matrix_size)]
            visited[i][j] += cafes[i][j]  # 초기값
            used_direction = []
            history = set()
            dfs(cafes, matrix_size, start, i, j, visited, used_direction, history)
    return


def main():
    T = int(input())
    
    for test_case in range(1, T+1):
        N = int(input())
        cafes = [list(map(int, input().split())) for _ in range(N)]
        
        cafe_tour(cafes, N)
        
        print(f"#{test_case} {max_dessert}")
        break


if __name__ == "__main__":
    main()