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


dxy = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
max_dessert = -1


def log(matrix):
    for lst in matrix:
        for elem in lst:
            print(elem, end=' ')
        print()
    print(f"max dessert:", max_dessert)
    print()


def dfs(matrix, n, start, x, y, i, visited, history):
    global max_dessert
    
    visited[x][y] = 1
    history.append(matrix[x][y])
    
    print(f"현좌표: {(x, y)}, history: {history}, i: {i}")
    log(visited)
    
    for dir_idx in range(i, i+1):
        dx, dy = dxy[dir_idx]
        nx, ny = x + dx, y + dy
        
        # 도착 지점 도달
        if start == (nx, ny) and len(history) >= 4:
            max_dessert = max(max_dessert, sum(history))
            print("도챠쿠")
            return
        
        # 배열 범위 벗어난 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        # 이미 방문한 경우
        if visited[nx][ny]:
            continue
        
        dfs(matrix, n, start, nx, ny, i+1, visited, history)
    
    visited[x][y] = 0
    history.pop()


def cafe_tour(cafes, size):
    for i in range(size):
        for j in range(size):
            start = (i, j)
            print("시작점", start)
            visited = [[0]*size for _ in range(size)]
            history = []
            dfs(cafes, size, start, i, j, 0, visited, history)
    return


def main():
    T = int(input())
    
    for test_case in range(1, T+1):
        N = int(input())
        cafes = [list(map(int, input().split())) for _ in range(N)]
        print(cafes)
        cafe_tour(cafes, N)
        
        print(f"#{test_case} {max_dessert}")
        break


if __name__ == "__main__":
    main()