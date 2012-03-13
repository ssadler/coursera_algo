import sys


def brutal(seq):
    """
    O(n*(n-1)/2)

    (n-1) + (n-2) + (n-3) + (n-4) + (n-5) ...

    INCIDENTALLY:
    The complexity above corresponds to the largest possible
    number of inversions!
    """

    n = 0

    for i in xrange(len(seq)):
        for j in xrange(i, len(seq)):
            if seq[i] > seq[j]:
                n += 1
                #print seq[i], seq[j]

    return n

#print brutal(map(int, sys.stdin))
print brutal([40, 32, 20, 88, 4, 93, 83, 77, 11, 75, 28, 8, 41, 27, 34, 79, 16, 76, 38, 28])
