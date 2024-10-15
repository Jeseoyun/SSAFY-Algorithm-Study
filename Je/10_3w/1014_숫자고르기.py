# 0 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 3 1 1 5 5 4 6

max_len_comb = []


def subset(numbs, key, key_comb):
    global max_len_comb

    if key == len(numbs):
        val_comb = set([numbs[k] for k in key_comb])

        if val_comb == set(key_comb) and len(val_comb) > len(max_len_comb):
            max_len_comb = val_comb
        return

    subset(numbs, key+1, key_comb)
    subset(numbs, key+1, key_comb+[key])


def main():
    N = int(input())
    numbs = {n+1: int(input()) for n in range(N)}

    subset(numbs, 1, [])

    print(len(max_len_comb))
    for i in max_len_comb:
        print(i)


if __name__ == "__main__":
    main()
