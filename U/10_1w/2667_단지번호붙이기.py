'''
https://www.acmicpc.net/problem/2667

bfs로 찾으면 될 거 같음
근데 하나 찾은 다음에 두 번째거는 어떤 식으로 찾아야 할지 모르겠네 지능이 낮아진다

있어야 하는 기능
1. 1의 좌표(단지 count 시작 좌표) 찾기
2. 단지 만들기
3. 단지 수 세기 => counter 모듈 써보자

'''
# from pprint import pprint
from collections import deque
from collections import Counter

N = int(input())

board = [list(input()) for _ in range(N)]
num = 11


def search(y, x):
    global board
    dyx = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    deq = deque([(y, x)])
    board[y][x] = num   # 방문 처리

    while deq:
        cy, cx = deq.popleft()

        for dy, dx in dyx:
            ny, nx = cy+dy, cx+dx   # 새로 이동할 칸

            if not (0 <= ny < N and 0 <= nx < N): continue  # 범위가 아닌 경우 넘어감

            # 단지인 경우(1)만 방문 처리 후 데큐에 넣음
            if board[ny][nx] == '1':
                board[ny][nx] = num
                deq.append((ny, nx))

    return


for i in range(N):
    for j in range(N):
        # 단지 시작 부분이면
        if board[i][j] == '1':
            # bfs 시작
            search(i, j)
            num += 1    # 단지 번호 증가

# pprint(board)

flat_board = sum(board, [])
# print(flat_board)
apt_dict = Counter(flat_board)

if '0' in apt_dict.keys():
    apt_dict.pop('0')  # 불필요한 부분 제거

res = sorted(apt_dict.values()) # value만 추출 후 정렬

print(len(res)) # 총 단지 수
for i in res:
    print(i)

