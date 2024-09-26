import sys
sys.stdin = open("Je\8_4w\input.txt")


'''
문제 링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu
'''


dxy = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
max_dessert = -1


def log(matrix):
    for lst in matrix:
        for elem in lst:
            print(elem, end=' ')
        print()
    print()


def dfs(matrix, n, start, x, y, i, visited, history):
    global max_dessert

    # 도착 지점 도달
    if start == (x, y) and len(history) >= 4:
        max_dessert = max(max_dessert, len(history))
        return
    
    for dir_idx in range(i, i+2):
        if dir_idx == 4:  
            break
        dx, dy = dxy[dir_idx]
        nx, ny = x + dx, y + dy
        
        # 배열 범위 벗어난 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        # 이미 방문한 경우
        if visited[nx][ny]:
            continue
        
        # 디저트 종류가 같은 카페가 이미 존재하는 경우
        if matrix[nx][ny] in history:
            continue
            
        visited[nx][ny] = 1
        history.append(matrix[nx][ny])

        # log(visited)
        
        dfs(matrix, n, start, nx, ny, dir_idx, visited, history)
    
        visited[nx][ny] = 0
        history.pop()


def cafe_tour(cafes, size):
    for i in range(size):
        for j in range(size):
            start = (i, j)
            visited = [[0]*size for _ in range(size)]
            history = []
            dfs(cafes, size, start, i, j, 0, visited, history)
    return


def main():
    T = int(input())
    
    for test_case in range(1, T+1):
        global max_dessert
        max_dessert = -1

        N = int(input())
        cafes = [list(map(int, input().split())) for _ in range(N)]
        cafe_tour(cafes, N)
        
        print(f"#{test_case} {max_dessert}")


if __name__ == "__main__":
    main()