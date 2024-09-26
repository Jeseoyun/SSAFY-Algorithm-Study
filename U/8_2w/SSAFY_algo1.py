'''
시간 복잡도 O(N)

숫자(유지보수 비용)가 나오기 전까지 나온 열린 대괄호의 개수가 해당 건물의 depth
열린 대괄호 수를 카운트 : depth_cnt
대괄호가 닫히면 해당 depth는 종료되는 것과 마찬가지
따라서 닫힌 대괄호가 나오면 depth_cnt를 1감소
숫자를 만나면 비용 해당 건물의 비용 계산 : 유지보수 비용 * depth_cnt
'''
import json
import sys
sys.stdin = open('algo1_sample_in.txt', 'r')

T = int(input())

def check_list(arr, depth_cnt):
    global total_cost
    for item in arr:
        # print(item)
        # 리스트인지 확인
        # 리스트인 경우 건물 깊이가 1 증가하고
        # 다시 리스트 체크
        if isinstance(item, list):
            depth_cnt += 1
            check_list(item, depth_cnt)
            # 해당 리스트를 모두 순회했다는 것은
            # 괄호가 닫혔다는 것과 동일함
            # 따라서 깊이를 1 감소시켜줌
            depth_cnt -= 1
        # 리스트가 아닌 경우 유지보수 비용 계산 
        else:
            total_cost += item * depth_cnt


for test_case in range(1, T+1):
    # 유지보수 비용의 요소 수: N
    N = int(input())
    # replace('문자1', '문자2) : 문자1을 문자2로 교체
    cost = json.loads(input().strip())
    depth_cnt = 1
    total_cost = 0  # 모든 건물 총 비용

    check_list(cost, depth_cnt)
            
    print(f'#{test_case} {total_cost}')
    
'''
    for i in range(len(cost)):
        if cost[i] == '[':
            # 열린 괄호라면 깊이 카운터 증가
            depth_cnt += 1
        elif cost[i].isdigit():
            # 숫자라면
            # 해당 건물의 비용 계산 후 전체 값 합침
            total_cost += int(cost[i]) * depth_cnt
        elif cost[i] == ']':
            # 닫힌 괄호라면 카운터 감소
            depth_cnt -= 1
'''

