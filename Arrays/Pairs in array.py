def countKdivPairs(A, k):
    count = 0
    sum = 0

    for i in range(0, len(A)):
        for j in range(i + 1, len(A)):
            sum = A[j] + A[i]

            if sum % k == 0:
                count += 1
    print(count)


countKdivPairs(A=[2, 2, 1, 7, 5, 3], k=4)
