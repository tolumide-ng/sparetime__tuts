#!/usr/bin/env python3

import os

v = """
-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0"""


def solution1(arr):
    # constrain min val = -9
    allcols = [i for i in arr.split('\n') if len(i)]
    all_the_col = [col.split(' ') for col in allcols]
    MAX = -9

    arr = []
    for i in all_the_col:
        spec_col = []
        for j in i:
            if len(j):
                spec_col.append(int(j))
        arr.append(spec_col)

    y = 0
    x = 0
    while x <= len(arr) - 3:
        while y <= len(arr[0]) - 3:
            sum = int(arr[y][x]) + int(arr[y][x + 1]) + int(arr[y][x + 2]) + int(arr[y+1]
                                                                                 [x+1]) + int(arr[y+2][x]) + int(arr[y + 2][x + 1]) + int(arr[y + 2][x + 2])

            MAX = max(MAX, sum)
            y += 1
        x += 1
        y = 0
    print(MAX)


if __name__ == '__main__':
    solution1("""    1 1 1 0 0 0

    0 1 0 0 0 0

    1 1 1 0 0 0

    0 0 2 4 4 0

    0 0 0 2 0 0

    0 0 1 2 4 0""")


def solution2():
    A = []
    for arr_i in range(6):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        A.append(arr_t)

    smax = -9 * 7

    for row in range(len(A) - 2):
        for column in range(len(A[row]) - 2):
            tl = A[row][column]
            tc = A[row][column + 1]
            tr = A[row][column + 2]
            mc = A[row + 1][column + 1]
            bl = A[row + 2][column]
            bc = A[row + 2][column + 1]
            br = A[row + 2][column + 2]
            s = tl + tc + tr + mc + bl + bc + br
            smax = max(s, smax)

    print(smax)
