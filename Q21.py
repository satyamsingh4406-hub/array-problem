def k_sma(arr,k):
    n=len(arr)
    lis=[]
    for i in range(n):
        if arr[i] not in lis:
            lis.append(arr[i])
    lis.sort()
    return lis[k-1]

arr=[2,4,5,6,2,1,3,5,7,4]
print(k_sma(arr,3))

