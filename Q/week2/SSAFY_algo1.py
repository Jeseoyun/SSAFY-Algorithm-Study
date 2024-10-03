'''
제가 생각한 문제의 핵심은 배열의 안쪽까지 들어가는 방법을 구현하는 것이 핵심이라 생각했습니다
제일 단순한 방법은 for문으로 계속 돌리면 될거 같은데? 라는 생각이 들면 어지간하면 그 문제들은
다 DFS였습니다. 이 문제도 for문으로 계속 들어가면 될 거 같은데? 라는 생각이 들어 그냥 DFS로 진행했습니다

'''
import json

# 글로벌로 접근하는 것이 좋지 않은 방법이기는 하나 재귀함수를 사용할 때는 global을 좀 많이 사용하는 편이라 그대로 진행하였습니다
answer = 0

def dfs(lst, depth):
    global answer
    for i in range(len(lst)):           # 종료 조건과 return을 따로 달지 않았는데 depth가 1일때 전체 배열의 길이로 for문을 시작했기 때문에 arr을 다 돌면 종료가 됩니다
        if isinstance(lst[i], int):     # 만일 인자가 int인 경우 덧셈을 진행하고
            answer += lst[i] * depth
        else:                           # 아닐 경우 list라는 얘기가 되므로 depth를 올리고 다음 dfs로 넘어갑니다
            dfs(lst[i], depth+1)


def main():
    global answer
    T = int(input())
    for test_case in range(1, T+1):
        N = int(input())
        arr = json.loads(input().strip())   # 이 함수가 리스트를 입력받는 함수로 사용하니 되게 편했습니다
        answer = 0                          # 전역변수를 사용할 경우 초기화 작업이 중요합니다

        dfs(arr, 1) # dfs의 첫 시작으로 입력받은 리스트 전체와 depth를 전달합니다

        print(f'#{test_case} {answer}')


if __name__ == "__main__":
    main()
