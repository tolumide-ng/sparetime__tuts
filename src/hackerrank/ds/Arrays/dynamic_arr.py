"""
    Create a list 'seqList' of N empty sequences where each sequence is indexed from 0 to N-1
            - The elements within each of the N sequences also use 0-indexing
            - Create an integer 'lastAnswer' and initiate it to 0
        -There are two types of queries that can be performed on the list of sequencies (seqList)
            1 => (1 x y)
                Find the sequence 'seq' at index ((x xor lastAnswer)%N) in seqList
                Append integer y to sequence seq
            2 => (2 x y)
                Find the sequence 'seq' at index ((x xor lastAnswer)%N) in seqList
                Find the value of y % size in seq (size = len(seq)) and assign it to lastAnswer
                Print the new value of lastAnswer on a newline
"""


# Two values are given at the beginning ==> 1. the number of sequences in seqList 2. the number of queries
N, Q = map(int, input().split())

lastAnswer = 0
seqList = [[] for _ in range(N)]

for _ in range(Q):
    # Values entered on each iteration
    q, x, y = map(int, input().split())
    index = (x ^ lastAnswer) % N
    seq = seqList[index]
    if q == 1:
        seq.append(y)
    elif q == 2:
        lastAnswer = seq[y % len(seq)]
        print(lastAnswer)
    else:
        raise ValueError()
