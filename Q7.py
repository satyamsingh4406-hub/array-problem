def rot(arr,k):
    return arr[k:]+arr[:k]

arr=[1,2,3,4,5,6,7,8,9]
n=int(input("Enter Your Range"))
print(rot(arr,n))
