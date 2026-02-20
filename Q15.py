def union(arr,brr):
    n=len(arr)
    na=len(brr)
    lis=[]
    for i in arr:
        if i not in brr:
            lis.append(i)
    for j in brr:
        if j not in arr:
            lis.append(j)
    return lis

arr1=[1,2,3,4,4,5,6,7]
arr2=[0,2,5,7,7,8,8]
print(union(arr1,arr2))