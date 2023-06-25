
def subarraySum(arr, k):
    sum = 0
    count = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
        if arr[i] == k:
            count += 1
        for j in range(i + 1, len(arr)):
            
            sum = sum + arr[j]
            if sum == k:
                count += 1
                sum = sum - arr[i]
            else:
                pass

    return count
    
arr = [1,1,1]
k=2
print(subarraySum(arr,k))
