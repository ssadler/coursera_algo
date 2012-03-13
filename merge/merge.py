import random

sample = lambda n: random.sample(range(100), n)

inversions = 0

def mergesort(arr):
    global inversions

    length = len(arr)

    if length == 1:
        return arr

    left = mergesort(arr[:length/2])
    right = mergesort(arr[length/2:])

    out = []

    while left and right:
        if left[0] < right[0]:
            out.append(left.pop(0))
        else:
            # inversions counts the number of places a number must
            # be moved relative to every other number
            inversions += len(left)
            out.append(right.pop(0))

    return out + left + right


def tinymerge(seq):
    if len(seq) < 2:
        return seq
    s1, s2 = tinymerge(seq[::2]), tinymerge(seq[1::2])
    return [min(s1, s2).pop(0) for _ in seq if s1 and s2] + s1 + s2
