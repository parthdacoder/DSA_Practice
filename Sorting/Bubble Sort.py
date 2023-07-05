def bubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            temp = arr[j]
            if arr[j] > arr[j + 1]:
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


print(bubbleSort(arr=[5, 2, 3, 4, 1, 7]))
