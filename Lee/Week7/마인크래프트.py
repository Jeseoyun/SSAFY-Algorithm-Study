# https://www.acmicpc.net/problem/18111 백준 마인크래프트
from Gom.마인크래프트 import min_height, max_height


# 회수 할거면 딱 다 하거나 놓기
# 원하는 높이에 맞는 블록 높이에 맞게 만들 수 있는 블록 개수가 된다면? 계산 ( 회수 과정 + 쌓는 과정)
# 제일 큰놈, 작은놈 말고 그냥 가능한 경우 다 찾아야하네
# 가능한 모든 높이를 안보고 key 값들로만 했었다가 엄청 헤멤

def solution(block_height, block):
    # 쌓는데 필요한 블록 개수
    block_time = 0
    sorted_dict = dict(sorted(block_dict.items(), key=lambda item: item[0], reverse=True))

    for key, value in sorted_dict.items():
        height_difference = block_height - key
        # 기준 높이보다 작으면
        if height_difference < 0:
            block_time += abs(height_difference) * value * 2
            block += abs(height_difference) * value
        # 기준 높이보다 높으면
        else :
            block_time += height_difference * value
            block -= height_difference * value

    # 갖고 있는것 보다 쌓을 블록이 더 많으면 X
    if block < 0:
        return -1

    return block_time


N, M, B = map(int, input().split())
block_arr = [list(map(int, input().split())) for _ in range(N)]

block_dict = {}

for i in range(N):
    for j in range(M):
        key = block_arr[i][j]
        if key not in block_dict.keys():
            block_dict[key] = 1
        else:
            block_dict[key] += 1

min_height = min(block_dict.keys())
max_height = max(block_dict.keys())
result_time, result_height = float('inf'), 0

# 모든 가능 높이를 반복문으로 돌며 최소 시간 계산
for target_height in range(min_height, max_height + 1):
    time = solution(target_height, B)
    if time >= 0:
        # 시간이 더 적으면 갱신
        if result_time > time:
            result_time = time
            result_height = target_height
        # 시간이 같으면 더 높은 땅을 선택
        elif result_time == time and result_height < target_height:
            result_height = target_height

if result_time == float('inf'):
    print(0, 0)
else:
    print(result_time, result_height)


# 1회
# # 가장 높은 거에 맞추기
# def make_all_high(block_height, block):
#     # 쌓는데 필요한 블록 개수
#     block_num = 0
#     for key, value in block_dict.items():
#         if key != block_height:
#             block_num = (block_height - key) * value
#
#     # 갖고 있는것 보다 쌓을 블록이 더 많으면 X
#     if block_num > block:
#         return 0
#
#     return block_num
#
#
# # 가장 낮은 거에 맞추기
# def make_all_lower(block_height):
#     block_num = 0
#     for key, value in block_dict.items():
#         if key != block_height:
#             block_num = abs((block_height - key)) * value * 2
#
#     return block_num
#
#
# N, M, B = map(int, input().split())
# block_arr = [list(map(int, input().split())) for _ in range(N)]
#
# # print(block_arr)
#
# block_dict = {}
#
# for i in range(N):
#     for j in range(M):
#         key = block_arr[i][j]
#         if key not in block_dict.keys():
#             block_dict[key] = 1
#         else:
#             block_dict[key] += 1
#
# # 제일 높은 층을 다 회수해서 제일 낮게 만들기 or
# # 다른 블록들을 채워서 제일 높은거랑 같게 만들기 => 블럭을 내가 갖고 있어야함
# # 비용 확인해서 작업 진행
#
# high_block = max(block_dict.keys())
# low_block = min(block_dict.keys())
#
# # 비용 확인
# result1 = make_all_high(high_block, B)
# result2 = make_all_lower(low_block)
# if result1 != 0:
#     # 가장 빠른놈, 같으면 높이가 높은놈 순
#     if result1 <= result2:
#         print(result1, high_block)
#     else:
#         print(result2, low_block)
# else:
#     print(result2, low_block)