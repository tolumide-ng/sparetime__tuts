"""
    - A 1-indexed array of zeros
    - For each operation `a b k` where add k to each array element from index a to b
    - Return the maximum value in the array
"""

n, m = map(int, input().split())


arr = [0]*n


for val in range(m):
    a, b, k = map(int, input().split())

    # while a <= b:
    #     arr[a - 1] += k
    #     a += 1
    #     print(arr)
    print(arr[a-1:])
    arr[a-1:] += k
    arr[b:] -= k

print(max(arr))
