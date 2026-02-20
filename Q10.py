def merg(arr,brr):
    n=len(arr)
    na=len(brr)
    i=j=0
    lis=[]
    while(i<n and j<na):
        if(arr[i]>brr[j]):
            lis.append(brr[j])
            j+=1
        else:
            lis.append(arr[i])
            i+=1
    while(i<n):
        lis.append(arr[i])
        i+=1
    while(j<na):
        lis.append(brr[j])
        j+=1
    return lis

arr1=[1,3,5,7,7,9,11]
arr2=[2,2,4,6,7,8]
print(merg(arr1,arr2))