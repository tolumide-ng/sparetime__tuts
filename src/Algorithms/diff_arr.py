#!/usr/bin/env python3


class DiffArray:
    def __init__(self):
        self.A = list(map(int, input().split()))
        self.n = len(self.A)
        print(self.n)
        self.D = list([0] * (self.n + 1))
        print(self.D)
        self.initialize()

    def initialize(self):
        self.D[0] = self.A[0]
        self.D[self.n] = 0

        for i in range(1, self.n):
            self.D[i] = self.A[i] - self.A[i - 1]

        self.update()

    def update(self):
        l, r, x = input().split()
        self.D[int(l)] += int(x)
        self.D[int(r) + 1] -= int(x)

        self.printArr()

    def printArr(self):
        arr = []
        for i in range(self.n):
            if i == 0:
                self.A[i] = self.D[i]
            else:
                self.A[i] = self.D[i] + self.A[i - 1]

            # print(self.A[i], end=' ')
            arr.append(self.A[i])
        print(' '.join(arr))


if __name__ == '__main__':
    DiffArray()
