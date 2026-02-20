def Sum(arr):
    n=len(arr)
    sum=0
    for i in arr:
        sum+=i
    return sum
arr=[1,2,4,3,1,5,2]
a=Sum(arr)
print(a)