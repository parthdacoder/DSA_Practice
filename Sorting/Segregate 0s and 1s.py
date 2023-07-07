def segregate0and1(arr):
    count0 = 0
    count1 = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count0 += 1
    for i in range(0, count0):
        arr[i] = 0
    count1 = len(arr) - count0
    for i in range(count0, len(arr)):
        arr[i] = 1

    return arr


print(segregate0and1([0, 0, 1, 1, 1, 1, 1, 0]))
