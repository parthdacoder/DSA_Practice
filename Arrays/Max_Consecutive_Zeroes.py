# To calculate maximum consecutive zeroes
def getMaxLength(arr):
    count = 0
    result = 0
    for i in range(0,len(arr)):
        if arr[i] != 0:
            count = 0
        
        else: 
            count += 1
            result  = max(count, result)
    return result

  
    
arr = [0,0,1,2,3,4,1,0,0,0]

print(getMaxLength(arr))
