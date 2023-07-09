def sortArrayByParity(nums):
    arr_odd = []
    arr_even = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            arr_even.append(nums[i])
        else:
            arr_odd.append(nums[i])

    nums[0 : len(arr_even)] = arr_even

    nums[len(arr_even) :] = arr_odd

    return nums


print(sortArrayByParity([3, 2, 1, 4]))
