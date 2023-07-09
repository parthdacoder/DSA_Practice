def printPairs(arr, sum):
    hashmap = {}

    for i in range(len(arr)):
        temp = sum - arr[i]
        if temp in hashmap:
            print("Yes")
            return
        x = hashmap[arr[i]] = i
    print("No")


printPairs(arr=[1, 4, 5, 7, 9], sum=11)
