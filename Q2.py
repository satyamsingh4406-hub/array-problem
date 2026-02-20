def min_max(arr):
    n=len(arr)
    max=0
    min=arr[0]
    for i in range(n):
        if(arr[i]>max):
            max=arr[i]
        if(min>arr[i]):
            min=arr[i]
    return max,min
arr=[1,2,4,2,3,5,6,8]
a=min_max(arr)
print(a)