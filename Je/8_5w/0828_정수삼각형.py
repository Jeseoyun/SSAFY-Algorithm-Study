def solution(triangle):    
    for i in range(len(triangle)):
        if i == 0: 
            continue
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i-1]):
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    return max(triangle[-1])


def main():
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    
    print(solution(triangle))


if __name__ == "__main__":
    main()