def rot_right(arr,k):
    return arr[-k:]+arr[:-k]

arr=[1,2,3,4,5,6,7]
n=int(input("Enter The Range: "))
print(rot_right(arr,n))