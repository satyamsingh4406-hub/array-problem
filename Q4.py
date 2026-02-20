def sec_max(arr):
    n=len(arr)
    Max=sec_max=0
    for i in range(n):
        if(arr[i]>Max):
            sec_max=Max
            Max=arr[i]
        elif(arr[i]>sec_max and arr[i]<Max):
            sec_max=arr[i]
    return sec_max

arr=[6,7,3,5,7,9,9,8,9]
a=sec_max(arr)
print(a)
