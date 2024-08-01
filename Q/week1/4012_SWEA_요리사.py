'''
강사님께서 진행하신 코드의 최적화를 진행해 보았습니다.
제가 생각한 문제의 핵심은
식재료들을 A와 B로 나누는 알고리즘이었습니다.

먼저 조합을 생성하는 방법은 itertools가 최상의 방법이라 이 부분은 그대로 진행하였습니다

그 다음 생성된 조합을 A와 B로 나누는 부분입니다
강사님이 진행하신 방법은 A에 itertools를 통해 나온 조합을 넣고 없는 숫자를 B에 넣는 방식으로 진행하셨습니다
이 부분에서 수행시간이 오래 걸리게 되어 이 부분을 바꾸기 위해 itertools로 나온 조합을 리스트로 변환하였고
세번째 테스트 케이스의 결과값을 확인해보니
(0, 1, 2), (0, 1, 3) ... (2, 4, 5), (3, 4, 5)와 같은 방식으로 생성되는 것을 확인할 수 있었습니다.

여기서 신기한 점을 발견하였는데 a리스트를 앞에서 읽고 b리스트를 뒤에서 읽게 되면 서로의 숫자가 겹치지 않는다는 점이였습니다

그래서 이 부분을 이용하여 코드를 구성하였습니다. 이렇게 코드를 구성하면 a리스트에 숫자가 있는지 확인하는 과정을 거치지 않게 되고
원하는 결과값이 A와 B의 최소 차이이므로 조합을 다 돌지 않고 절반만 돌더라도 모든 계산을 수행할 수 있습니다.
'''


import itertools


def calculate_synergy(food_list, synergy):
    total_synergy = 0
    for i in range(len(food_list)):             # a리스트에 들어온 값인 (0,1,2)를 예시로 하자면 시작 i 값은 0이 됩니다
        for j in range(i + 1, len(food_list)):  # j는 i+1부터 시작하기에 더하는 값은 (0,1)과 (1,0)의 값을 더하게 됩니다. 후에 j가 1이 증가해 (0,2) (2,0)을 더한 후 (1,2) (2,1)을 계산하여 중복되는 값 없이 합계 계산이 완료됩니다
            total_synergy += synergy[food_list[i]][food_list[j]] + synergy[food_list[j]][food_list[i]]
    return total_synergy


T = int(input())
for test_case in range(1, T + 1):
    # 입력 받는 과정
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    # 식재료를 절반으로 나눌 예정이고 N은 짝수라는 점이 문제에서 주어짐
    half = N // 2

    # itertools.combinations를 사용하기 위해서는 리스트가 필요하기에 리스트 생성
    num_list = [i for i in range(N)]
    food_comb_list = list(itertools.combinations(num_list, half)) # 조합 생성
    res = float('inf') # 최소값을 도출하기 위해서 초기값은 줄 수 있는 최대값으로 줘야함 inf가 헷갈릴 경우 12345678도 좋습니다

    for i in range(len(food_comb_list) // 2):   # 위에서 설명한 대로 생성된 조합 리스트의 절반만 돌면 됩니다
        a_food_list = food_comb_list[i]         # a food 리스트는 조합 리스트의 값을 앞에서부터 넣습니다
        b_food_list = food_comb_list[-i - 1]    # b food 리스트는 조합 리스트의 값을 뒤에서부터 넣습니다

        a_synergy_sum = calculate_synergy(a_food_list, synergy)     # sum을 계산하는 과정은 a와 b가 같기에 과정을 함수로 빼줍니다 24번 라인으로 이동
        b_synergy_sum = calculate_synergy(b_food_list, synergy)

        res = min(res, abs(a_synergy_sum - b_synergy_sum))          # 현재까지 나왔는 result값과 계산을 진행하였는 값 중 작은 값을 result값으로 가집니다

    print(f'#{test_case} {res}')
