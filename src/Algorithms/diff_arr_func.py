#!/usr/bin/env python3


def initalizeDiffArr(A):
    n = len(A)

    D = [0]*(n+1)

    D[0] = A[0]
    D[n] = 0

    for i in range(1, n):
        D[i] = A[i] - A[i - 1]
    return D


def update(D, l, r, x):
    D[l] += x
    D[r + 1] -= x


def printArr(A, D):
    j = ''
    for i in range(0, len(A)):
        if i == 0:
            A[i] = D[i]
        else:
            A[i] = D[i] + A[i - 1]

        print(A[i], end=' ')
        #     j + str(A[i]) + ' '
        # print(j.strip())


if __name__ == '__main__':
    a = list(map(int, input().split()))

    d = initalizeDiffArr(a)

    update(d, 2, 4, 43)
    print('VALUE OF A', a)
    print('Value of d', d)

    printArr(a, d)
