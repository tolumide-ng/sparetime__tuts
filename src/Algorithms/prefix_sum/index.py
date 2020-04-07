def prefix_sum(A):
    n = len(A)
    P = [0] * (n + 1)

    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P
