#!/usr/bin/env python3


def left_rotation():
    n, d = input().split()
    v = map(int, input().split())

    arr = [val for val in v]

    new_arr = arr

    for _ in range(int(d)):
        new_arr.append(new_arr[0])
        new_arr = new_arr[1:]
    print(*new_arr, sep=' ')


if __name__ == '__main__':
    left_rotation()
