def log(arr):
    for lst in arr:
        for elem in lst:
            print(elem, end=' ')
        print()
    print()


# 개선 전 version
def old_solution(m, n, puddles):
    path = [[1]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if [i+1, j+1] in puddles:
                path[i][j] = 0
            elif i-1 < 0:
                path[i][j] = path[i][j-1]
            elif j-1 < 0:
                path[i][j] = path[i-1][j]
            else:
                path[i][j] = path[i][j-1] + path[i-1][j]
                
    return path[n-1][m-1] % 1000000007


# 개선 version
# 1. puddles를 set 자료형으로 바꾸어 in 연산시간 단축 (O(n) -> O(1))
# 2. if문에서 중복되는 부분 합쳐서 코드 가독성 향상
def solution(m, n, puddles):
    puddles = set(tuple(p) for p in puddles)
    
    if (1, 1) in puddles or (m, n) in puddles:
        return 0
    
    path = [[0]*m for _ in range(n)]
    path[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if (j+1, i+1) in puddles:
                path[i][j] = 0
            else:
                if i > 0:
                    path[i][j] += path[i-1][j]
                if j > 0:
                    path[i][j] += path[i][j-1]
                
    return path[n-1][m-1] % 1000000007


def main():
    m, n = 4, 3
    puddles = [[2, 2]]
    
    print(solution(m, n, puddles))


if __name__ == "__main__":
    main()
