min_height = float("inf")

def dfs(heights, max_height, cur_h, idx):
    global min_height

    if cur_h >= max_height:
        min_height = min(cur_h, min_height)
        return
    
    if idx >= len(heights):
        return
    
    dfs(heights, max_height, cur_h + heights[idx], idx + 1)
    dfs(heights, max_height, cur_h, idx + 1)


def main():
    T = int(input())
    
    for test_case in range(1, T + 1):
        global min_height
        min_height = float("inf")

        num, max_height = map(int, input().split())
        heights = list(map(int, input().split()))

        dfs(heights, max_height, 0, 0)

        print(f"#{test_case} {min_height - max_height}")


if __name__ == "__main__":
    main()