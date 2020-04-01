#!/usr/bin/env python3

import os

# SOLUTION 0


def solution0(val):
    with open('result.txt', 'w') as f:
        f.write(str(len(val.split(' '))))
        f.write('\n')
        f.write(' '.join(val.split(' ')[::-1]))


solution0('1 4 3 2')


# SOLUTION 1
def solution1():
    int(input().strip())
    A = input().split(' ')
    B = []
    for val in reversed(A):
        B.append(val)
    print(' '.join(B))


# SOLUTION 2
def solution2():
    int(input().strip())
    A = input().split()
    length = len(A) - 1
    val = []
    while length >= 0:
        val.append(A[length].strip())
        length -= 1
    print(' '.join(val))


# SOLUTION 3
def solution3():
    N = int(input().strip())
    A = input().split(' ')
    A.reverse()
    print(' '.join(A))


# SOLUTION 3
if __name__ == '__main__':
    solution1()
