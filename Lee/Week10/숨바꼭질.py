# # https://www.acmicpc.net/problem/1697 숨바꼭질
# # 만약 수빈이 X, 1초후에 X-1 or X+1
# # 순간이동 1초 후에 2*X
# # 동생이 수빈이보다 앞에 있으면 +1 or 순간이동
# # else - 1
# # 일단 dfs 해볼까? ㄴㄴ
# # 2배로 최대한 동생한테 가까이 가는게 좋음
# # 내 위치 앞 뒤 한칸씩, 2배 한게 동생 위치 짝수에 제일 빨리 도착하면
# # 계속 2배하고 차이 계산하면서 가까워 지는거 확인하고, 오히려 멀어지면 갱신 그만
#
#
# N, K = map(int, input().split())
# count = -1
# start_num = -1
#
# if K % 2 == 0:
#     # 수빈이 앞,뒤 1 / 현 위치에서 2배씩
#     for n in range(N-1, N+2):
#         # 시작할 때 거리 차이
#         dist = abs(K - N)
#         c = 0
#
#         while True:
#             # 현재 위치에서 2배하고 거리 차이
#             double_dist = abs(K - n * 2)
#
#             # 2배해서 도착
#             if double_dist == 0:
#                 start_num = n
#                 break
#
#             # 1차이
#             elif double_dist == 1:
#                 start_num = n
#                 break
#
#             # 2배 거리 차이가 더 줄었으면
#             if double_dist < dist:
#                 c += 1
#                 # 현재 위치 갱신
#                 dist = double_dist
#                 n *= 2
#
#             else:
#                 break
#
#         if c > count:
#             start_num = n
#
# print(start_num)
