def checkIsAP(A):
    A.sort()

    d = A[1] - A[0]
    for i in range(2, len(A)):
        if A[i] - A[i - 1] != d:
            return False
    return True


print(checkIsAP(A=[20, 15, 5, 0, 10]))
