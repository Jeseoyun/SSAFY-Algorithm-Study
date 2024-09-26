# '''
# BFS로 풀려다가 실패
# 현재 고려해야할 것 k에 도달했을 경우 종료 어떻게?
# cur_time만 가지고는 어떻게 2에서 시작한 애들 체크를 어떻게 할 것인가
# 결국 우선순위 q를 써야한다 or cur_time에 cur_val만큼 더해서 stack에 때리면
# 결국 그 아이가 실행되는 시점의 cur_time = 진행된 시간이 된다를 이용해 보기
#
#
# '''
# from collections import deque
#
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
#
# T = int(input())
# for test_case in range(1, T + 1):
#     n, m, k = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     q = deque()
#     q2 = deque()
#
#     arr_dict = {}
#     arr_dict2 = {}
#
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] != 0:
#                 arr_dict[(i, j)] = arr[i][j]
#                 q.append((i, j, arr[i][j], arr[i][j]))
#
#     for time in range(k):
#         while q:
#             cur_x, cur_y, cur_val, cur_time = q.popleft()
#
#             if cur_time != 0:
#                 q2.append((cur_x, cur_y, cur_val, cur_time - 1))
#                 continue
#
#             for i in range(4):
#                 nx = cur_x + dx[i]
#                 ny = cur_y + dy[i]
#
#                 if (nx, ny) in arr_dict and arr_dict[(nx, ny)] >= cur_val:
#                     continue
#                 if (nx, ny) in arr_dict and arr_dict[(nx, ny)] == 0:
#                     continue
#
#                 # arr_dict[(nx, ny)] = cur_val
#                 # q2.append((nx, ny, cur_val, cur_val))
#                 arr_dict[(cur_x, cur_y)] = 0
#                 if (nx, ny) in arr_dict2 and arr_dict2[(nx, ny)] >= cur_val:
#                     continue
#                 else:
#                     arr_dict2[(nx, ny)] = cur_val
#
#         for key, value in arr_dict2.items():
#             nx, ny = key
#             cur_val = value
#             arr_dict[(nx, ny)] = cur_val
#             q2.append((nx, ny, cur_val, cur_val))
#         arr_dict2.clear()
#
#         while q2:
#             cur_x, cur_y, cur_val, cur_time = q2.popleft()
#             q.append((cur_x, cur_y, cur_val, cur_time))
#
#     answer = {}
#     while q:
#         cur_x, cur_y, cur_val, cur_time = q.popleft()
#         answer[(cur_x, cur_y)] = 1
#
#     print(f'#{test_case} {len(answer)}')

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    q = deque()
    q2 = deque()

    arr_dict = {}
    vis = {}

    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                arr_dict[(i, j)] = arr[i][j]
                q.append((i, j, arr[i][j], arr[i][j]))
                vis[(i, j)] = 1

    for time in range(k):
        while q:
            cur_x, cur_y, cur_val, cur_time = q.popleft()
            vis[(cur_x, cur_y)] = 1
            if cur_time != 0:
                q2.append((cur_x, cur_y, cur_val, cur_time - 1))
                continue

            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]

                if (nx, ny) in arr_dict and arr_dict[(nx, ny)] >= cur_val:
                    continue
                if (nx, ny) in arr_dict and arr_dict[(nx, ny)] == 0:
                    continue
                if (nx, ny) in vis and vis[(nx, ny)]:
                    continue

                arr_dict[(nx, ny)] = cur_val
                q2.append((nx, ny, cur_val, cur_val))
                arr_dict[(cur_x, cur_y)] = 0

        while q2:
            cur_x, cur_y, cur_val, cur_time = q2.popleft()
            q.append((cur_x, cur_y, cur_val, cur_time))

    answer = {}
    while q:
        cur_x, cur_y, cur_val, cur_time = q.popleft()
        answer[(cur_x, cur_y)] = 1

    print(f'#{test_case} {len(answer)}')
