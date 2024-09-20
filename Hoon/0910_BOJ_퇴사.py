def main():
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(num)]

    dp = [0] * (num + 1)

    for day in range(0, num):
        duration = arr[day][0]
        value = arr[day][1]

        if day + duration > num:
            continue

        dp[day + duration] = max((dp[day] + value), dp[day + duration])
        
        for i in range(day + duration, num+1):
            dp[i] = max(dp[i], dp[i-1])
        
        #print(dp)
    print(dp[-1])


if __name__ == "__main__":
    main()