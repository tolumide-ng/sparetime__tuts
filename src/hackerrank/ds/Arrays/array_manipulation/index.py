#!usr/bin/env python3


class ArrayManupluation:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.d = {}
        self.initialize()

    def initialize(self):
        for _ in range(0, self.m):
            a, b, k = map(int, input().split())

            self.d.setdefault(a, 0)
            self.d[a] = self.d[a] + k

            if b <= self.n + 2:
                self.d.setdefault(b + 1, 0)
                self.d[b + 1] = self.d[b + 1] - k

        maxx = 0
        x = 0
        for i in sorted(self.d):
            x += self.d[i]
            if (maxx < x):
                maxx = x
        print(maxx)


if __name__ == '__main__':
    ArrayManupluation()
