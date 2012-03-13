
inversions = 0

def mergesort(arr):
    global inversions

    length = len(arr)

    if length == 1:
        return arr

    left = mergesort(arr[:length/2])
    right = mergesort(arr[length/2:])

    out = []

    while True:
        if left and right:
            if left[0] > right[0]:
                inversions += len(left)
                out.append(right.pop(0))
            else:
                out.append(left.pop(0))
        else:
            if left:
                out += left
            elif right:
                out += right
            break

    return out



print inversions



def minimerge(s1, s2):
    if s1 and s2:
        return [min(s1, s2).pop(0)] + minimerge(s1, s2)
    return s1 + s2

def minimergesort(seq):
    return minimerge(mergesort(seq[::2]), mergesort(seq[1::2]))



print minimergesort([40, 32, 20, 88, 4, 93, 83, 77, 11, 75, 28, 8, 41, 27, 34, 79, 16, 76, 38, 28])