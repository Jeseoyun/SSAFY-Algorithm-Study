from collections import defaultdict

# 첫 번째 줄 숫자 : 두 번째 줄 숫자 형식으로 딕셔너리 생성
N = int(input())
num_dict = defaultdict()
for i in range(1, N+1):
    num_dict[i] = int(input())

# 각 줄에 대해서 중복되는 수를 제거
first_line = set(num_dict.keys())
second_line = set(num_dict.values())

while first_line != second_line:
    for i in first_line:
        # 두 번째 줄에 없는 숫자면 딕셔너리에서 제거
        if i not in second_line:
            del num_dict[i]

    first_line = set(num_dict.keys())
    second_line = set(num_dict.values())

print(len(first_line))
[print(i) for i in first_line]