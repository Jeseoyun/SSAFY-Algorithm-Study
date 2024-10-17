# https://www.acmicpc.net/problem/2668 숫자고르기
# 개수가 제일 많아야 함
# 본인하고 같은건 일단 무조건 추가
# 같은 집합인건 어차피 최대 2개니까 찾으면 바로 멈췃!
# 결과 : 뽑힌 정수 개수 , 오름차순
# # 같은 집합인거 찾으면 바로 종료
# for i in range(N):
#     for j in range(N):
#         if arr[i] == num_list[j] and num_list[i] == arr[j]:
#             result.add(i+1)
#             # result.append(j)
#             break
#
# for k in range(N):
#     if k+1 == arr[k]:
#         result.add(k+1)


# 뭐야 선택된거 집합이 진짜 집합 말한거였음 최대 2가 아님
# dfs로 집합 만들 수 있는 경우 다 해보다가 탈출로 max 보다 작으면 멈춰야지
# 앞으로 확인할 수가 set2 개수에 더해도 작으면

def solution(set1, set2, idx):
    global result

    # 앞으로 확인할 수 있는 최대 개수가 현재 결과보다 적으면 종료
    if len(set1) + (N - idx) <= len(result):
        return

    # 끝까지 다 돌면
    if idx == N:
        # 두 집합이 다르면 종료
        if set1 != set2:
            return

        # 최대 크기의 집합 업데이트
        if len(result) < len(set1):
            result = set1.copy()  # 깊은 복사 대신 얕은 복사 사용
        return

    # 값 추가 후 재귀 호출
    set1.add(num_list[idx])
    set2.add(arr[idx])
    solution(set1, set2, idx + 1)

    # 백트래킹: 재귀 호출 후 원래 상태로 되돌림 (다음 경우를 위해)
    set1.discard(num_list[idx])  # KeyError를 방지하기 위해 discard 사용
    set2.discard(arr[idx])       # KeyError를 방지하기 위해 discard 사용

    # 값 추가하지 않은 상태로 재귀 호출
    solution(set1, set2, idx + 1)


N = int(input())
num_list = list(range(1, N+1))
arr = [int(input()) for _ in range(N)]

result = set()

solution(set(), set(),0)

result = list(result)
result.sort()

print(len(result))
for val in result:
    print(val)