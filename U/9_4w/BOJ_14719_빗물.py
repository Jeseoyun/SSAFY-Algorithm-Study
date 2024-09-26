'''
https://www.acmicpc.net/problem/14719

음 하나도 모르겠고

0번과 W-1 인덱스에는 물이 고일 수 없다
---
세로로 한 칸씩 보자
세로 한 줄에 물이 고이기 위해서는 해당 위치의 벽보다 높은 벽이 좌우에 있어야 함

'''

H, W = map(int, input().split())
brick = list(map(int, input().split()))
result = 0


# 좌우의 좌우의 가장 높은 벽 찾기
def find_wall(idx):
    left_max_height = 0
    right_max_height = 0

    # 왼쪽 벽 찾기
    for left_idx in range(idx-1, -1, -1):
        left_max_height = max(left_max_height, brick[left_idx])

    for right_idx in range(idx+1, W):
        right_max_height = max(right_max_height, brick[right_idx])

    return left_max_height, right_max_height


for i in range(1, W-1):
    left_wall, right_wall = find_wall(i)
    # print(left_wall, right_wall, brick[i])

    # 어느 한 쪽이라도 자신보다 높은 벽이 없다면 빗물이 고일 수 없으므로 다음으로 넘어감
    if left_wall <= brick[i] or right_wall <= brick[i]: continue

    result += min(left_wall, right_wall) - brick[i]
    # print('->', result)
print(result)