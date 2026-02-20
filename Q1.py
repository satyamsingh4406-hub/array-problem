def rev(arr):
    n=len(arr)
    for i in range(n-1,-1,-1):
        print(arr[i])

arr=[12,32,4,1,2,3,4,5]
rev(arr)