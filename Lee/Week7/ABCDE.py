# https://www.acmicpc.net/problem/13023 백준 ABCDE

# dict에 노드번호를 KEY, 친구들을 Value로 저장
# 타고타고 들어가면서 친구의 친구 위아더 원~ 5명 이상이면 1 아니면 0

def solution(start_friend, count, temp_list):
    global result

    if count == 5:
        # print(temp_list)
        result = 1
        return

    # 친구가 없으면 반환
    if not friend_dict[start_friend]:
        return

    # 시작 노드의 친구들로 넘어가는 과정
    for next_key in friend_dict[start_friend]:
        # start_friend가 아는 친구중에 temp_list에 없고 아직 ABCDE를 못 찾은 상태면
        if next_key not in temp_list and result != 1:
            solution(next_key, count + 1, temp_list + [next_key])

N, M = map(int, input().split())
friend_dict = {}
# 0~N-1 까지 키값에 빈 리스트 생성
for friend_name in range(N):
    friend_dict[friend_name] = []

# key에 친구들 서로 넣기 양방향 친구임
for i in range(M):
    key, value = map(int, input().split())
    friend_dict[key].append(value)
    friend_dict[value].append(key)

result = 0

# 시작을 다르게해서 ABCDE 되는 경우 찾기
for start_node in range(N):
    if result == 0:
        solution(start_node, 1, [start_node])
    else:
        break

print(result)