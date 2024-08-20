import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

# x, y 축으로 이동 시 계산 배열(상하우좌)
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
# 배열 크기 할당
m, n = 16, 16

def bfs(x,y):
    # 큐 생성 및 시작 지점 입력
    q = deque([(x, y)])

    # 방문여부 확인 배열, 미방문 시 False
    visited = [[False] * m for _ in range(n)]

    # 시작 지점 방문 완료
    visited[x][y] = True

    # q에 값이 없을때까지 반복
    while q:
        # 큐의 맨 앞 값을 빼와 x, y에 저장
        x, y = q.popleft()

        # 상하우좌 이동
        for dx, dy in dxy:
            nx, ny = dx + x, dy + y

            # nx, ny가 배열 값 이내 좌표이고 방문하지 않은 지점이면서 벽이 아닌곳
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] != 1:
                q.append((nx, ny))
                visited[nx][ny] = True

            # 도착 지점 도착시
            if arr[nx][ny] == 3:
                return 1
    # 도착점 도착 불가 시
    return 0


for _ in range(1, 11):
    # 테스트 케이스 번호 입력 받음
    T = int(input())

    # 16x16 미로 배열을 입력 받음
    arr = [list(map(int, input())) for _ in range(16)]

    # 결과값 출력
    print(f'#{T} {bfs(1, 1)}')