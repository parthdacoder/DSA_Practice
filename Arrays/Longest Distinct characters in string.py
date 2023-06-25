
def areDistinct(stri):
    result = 0

    for i in range(len(stri)):
        mid = ''
        mid = mid + stri[i]
        count = 1

        for j in range(i + 1, len(stri)):
            if stri[j] not in mid:
                mid = mid + stri[j]
                count += 1
            else:
                    break
            
        if count > result:
                result = count
    return result
    
                    


stri = 'GEEKSFORGEEKS'
print(areDistinct(stri))
