# i를 기준으로 (i보다 왼쪽에 있는 값 중 제일 큰 값, i보다 오른쪽에 있는 값 중 제일 큰 값)
# 이 두가지 값 중 작은 값 - arr[i]가 빗물의 양
# ex) 10 0 6 0 8 현재 i가 2일때  왼쪽 값 중에서는 arr[0]의 10이 가장 크고 오른쪽 값 중에서는 arr[4]의 8이 가장 크므로 arr[2]에는
# 8 - 6 = 2만큼의 빗물이 차오른다

h, w = map(int, input().split())
arr = list((map(int, input().split())))
i = 0
answer = 0

while i < w and arr[i] == 0:
    i += 1

i += 1                      # 현재 i값은 벽이 시작되는 제일 왼쪽 값이므로 i+1을 한 후 시작

while i < w-1:
    left_max = max(arr[0:i])
    right_max = max(arr[i+1:w])

    temp = min(left_max, right_max)

    if arr[i] < temp:
        answer += temp - arr[i]
    i += 1

print(answer)