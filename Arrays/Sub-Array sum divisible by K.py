def subCount(arr, k):
    count = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j] 
            if sum%k == 0:
                count += 1
    print(count)
                
arr = [4, 5, 0, -2, -3, 1]
k = 5

subCount(arr,k)