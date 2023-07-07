def sort012(arr):
    count0 = 0
    count1 = 1
    count2 = 2

    for i in range(len(arr)):
        if arr[i] == 0:
            count0 += 1
    for i in range(0, count0):
        arr[i] = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            count1 += 1
    count2 = len(arr) - (count0 + count1)
    y = len(arr) - count2

    for i in range(count0, y):
        arr[i] = 1

    for i in range(y, len(arr)):
        arr[i] = 2

    return arr


print(sort012([1, 2, 0, 0, 0, 2, 0, 1, 2, 1, 0]))
