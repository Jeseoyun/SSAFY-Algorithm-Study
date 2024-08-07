'''
문제링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB
난이도: D3
'''


def main():
    T = int(input())
    
    for test_case in range(1, T+1):
        N = int(input())  # arr size
        
        field = [list(map(int, input())) for _ in range(N)]
        mid = N//2
        
        result = 0
        for i in range(N):
            for j in range(N):
                # 중심(mid, mid)으로부터 (x, y)로 떨어진 거리가 mid 이내인 모든 점을 모으면 다이아몬드 모양이 됨
                if abs(mid-i) + abs(mid-j) <= mid:
                    result += field[i][j]
        print(f"#{test_case} {result}")    


if __name__ == "__main__":
    main()