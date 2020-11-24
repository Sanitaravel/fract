from itertools import groupby


def gen_next(arr, n):
    if n == 0:
        return arr
    else:
        tmp = []
        x = groupby(arr)
        for key, group_items in x:
            tmp.append(sum(1 for x in group_items))
            tmp.append(key)
        return gen_next(tmp, n-1)


def main():
    arr = [1]

    n = int(input("Input number of iteration: "))

    ans = gen_next(arr, n-1)
    for i in ans:
        print(i, end='')


if __name__ == '__main__':
    main()
