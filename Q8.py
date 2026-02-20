def pair_sum(arr, tar):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == tar:
                return arr[i], arr[j]
    return False

arr=[1,2,3,4,5,6,7,8,9]
target=int(input("Enter The Range: "))
print(pair_sum(arr,target))