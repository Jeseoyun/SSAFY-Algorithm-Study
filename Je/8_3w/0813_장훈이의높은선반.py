import sys
sys.stdin = open("Je/8_3w/input.txt")


'''
문제 링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw

점원들 키의 합으로 선반 높이보다 큰 숫자를 만들어야 함
-> 점원들 키로 만들 수 있는 부분집합 구하기
'''

def height_comb(idx, arr, threshold, comb, result):
    if idx == len(arr):
        if threshold <= sum(comb):  # 합이 선반 높이보다 클 때만 저장
            result.append(sum(comb))
        return

    # 현재 점원 포함 X
    height_comb(idx+1, arr, threshold, comb, result)

    # 현재 점원 포함 O
    height_comb(idx+1, arr, threshold, comb + [arr[idx]], result)

def main():
    T = int(input())

    for test_case in range(1, T+1):
        N, B = map(int, input().split())  # 점원 수, 선반 높이
        heights = list(map(int, input().split()))

        result = []
        height_comb(0, heights, B, [], result)

        print(f"#{test_case} {min(result) - B}")
    

if __name__ == "__main__":
    main()