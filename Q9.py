def remov(arr):
    n=len(arr)
    lis=set()
    for i in range(n):
        lis.add(arr[i])
    return lis

def rem_dup(arr):
    n=len(arr)
    lis=[]
    for i in range(n):
        if arr[i] not in lis:
            lis.append(arr[i])
    return lis

arr=[1,1,2,3,4,2,4,25,23,12,1,23,25]
print(rem_dup(arr))
print(remov(arr))