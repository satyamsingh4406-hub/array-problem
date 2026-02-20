def peak(arr):
    n=len(arr)
    if(arr[0]>arr[1]):
        return arr[0]
    if(arr[n-1]>arr[n-2]):
        return arr[n-1]
    for i in range(1,n-1):
        if(arr[i-1]<arr[i]>arr[i+1]):
            return arr[i]

arr=[10,11,13,24,9]
print(peak(arr))