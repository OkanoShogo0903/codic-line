import itertools

def qs(A):
    return A if len(A) <= 1 else\
            qs([x for x in A[:-1] if x <= A[-1]])\
            + A[-1:] +\
            qs([x for x in A[:-1] if x > A[-1]])\

if __name__ == '__main__':
    l = [11, 7, 8, 7, 2, 21, 31, 5, 3, 1]
    print("before :", l)        # before : [11, 7, 8, 7, 2, 21, 31, 5, 3, 1]
    print("after  :", qs(l))    # after  : [1, 2, 3, 5, 7, 7, 8, 11, 21, 31]

