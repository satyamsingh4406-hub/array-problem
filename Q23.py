def maxsub(arr):
    max_sum = arr[0]
    curr_sum = 0

    for num in arr:
        curr_sum += num
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_sum

arr=[1,2,3,4,5,6]
print(maxsub(arr))