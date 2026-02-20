def check_sor(arr):
    n=len(arr)
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            return False
    return True

arr=[1,2,3,4,5,6,7,9,11,23]
print(check_sor(arr))