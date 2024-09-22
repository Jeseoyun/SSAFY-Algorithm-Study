# https://www.acmicpc.net/problem/14719 빗물
import pprint

H, W = map(int, input().split())
height = list(map(int, input().split()))
result = 0
temp_result = 0

# 배열 생성 및 높이에 맞게 값 넣기
arr = [[0] * W for _ in range(H)]
temp_list = height[:]
for i in range(H-1, -1, -1):
    for idx, h in enumerate(height):
        if h >= 1:
            arr[i][idx] = 1
            temp_list[idx] -= 1
            height = temp_list[:]

# pprint.pprint(arr)
# 1 나오고 다음 1나올때가지 세서 더함
for q in range(len(arr)):
    for j in range(len(arr[q])-1):
        if arr[q][j] == 1:
            for k in range(j+1, len(arr[q])):
                if arr[q][k] == 1:
                    result += temp_result
                    temp_result = 0
                    break
                else:
                    temp_result += 1
    temp_result = 0
    # print(result)

print(result)