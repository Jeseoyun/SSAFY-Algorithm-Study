# # 흑흑
# H, W = map(int, input().split())
# blocks = list(map(int, input().split()))
# pre_max = -1
# pre_max_idx = -1
# total_water = 0
#
# for idx in range(W):
#     print(blocks)
#     if pre_max == -1:
#         pre_max = blocks[idx]
#         pre_max_idx = idx
#         continue
#
#     # 직전 블록보다 현재 블록이 더 높으면 평탄화 작업 해주기
#     if blocks[idx-1] < blocks[idx]:
#         # 1) 이전에 가장 높았던 블록보다 현재 블록이 높은 경우
#         if pre_max < blocks[idx]:
#             # 평탄화 작업 영역 구하기
#             h = pre_max - blocks[idx-1]  # 더 낮은 놈의 높이로 맞춰줘야 함
#             w = idx - pre_max_idx - 1  # 평탄화 작업 진행할 가로 길이
#             print(f"h: {h}, w: {w}")
#
#             total_water += (h * w)
#
#             # 평탄화 한 곳의 높이 갱신
#             for renew_idx in range(pre_max_idx+1, idx):
#                 blocks[renew_idx] = blocks[renew_idx] + h
#
#             # 가장 높은 지점 갱신
#             pre_max = blocks[idx]
#             pre_max_idx = idx
#
#         # 2) 현재 블록이 더 낮거나 높이 같은 경우
#         else:
#             h = blocks[idx] - blocks[idx-1]
#             w = idx - pre_max_idx - 1
#             print(f"h: {h}, w: {w}")
#             total_water += (h * w)
#
#             for renew_idx in range(pre_max_idx+1, idx):
#                 blocks[renew_idx] = blocks[renew_idx] + h
#
#             # 만약 이전에 가장 높은 지점과 현재 가장 높은 지점이 같으면
#             # 블록들이 완벽히 평탄화 되었으므로 max값을 초기화시켜준다
#             if pre_max == blocks[idx]:
#                 pre_max = -1
#                 pre_max_idx = -1
#
# print(blocks)
# print(total_water)


H, W = map(int, input().split())
blocks = list(map(int, input().split()))

left_max = [0] * W
right_max = [0] * W

# 1) 왼쪽부터 가장 높은 블록 기록
left_max[0] = blocks[0]

for i in range(1, W):
    # 현재 블록과 이전까지의 가장 높은 블록 중 더 큰 값을 저장
    left_max[i] = max(left_max[i-1], blocks[i])

# 2) 오른쪽부터 가장 높은 블록 기록
right_max[W-1] = blocks[W-1]

for i in range(W-2, -1, -1):
    # 현재 블록과 이후 블록들 중 가장 높은 블록 중 더 큰 값을 저장
    right_max[i] = max(right_max[i+1], blocks[i])

# 3) 각 블록에 고일 수 있는 물의 양 계산
total_water = 0  # 총 고인 물의 양

for i in range(W):
    # 해당 블록에 고일 수 있는 물의 양
    # (좌우에서 가장 높은 블록 중 더 작은 값) - (현재 블록의 높이)
    curr_water = min(left_max[i], right_max[i]) - blocks[i]

    # 고일 수 있는 물의 양이 양수인 경우에만 더함
    if curr_water > 0:
        total_water += curr_water

print(total_water)