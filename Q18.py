def mov_zer(arr):
    n=len(arr)
    lis=[]
    i=0
    while(i<n):
        if arr[i]!=0:
            lis.append(arr[i])
        i+=1
    for i in arr:
        if(i==0):
            lis.append(i)
    return lis

arr=[1,3,0,5,0,3,0,2,0]
arr=mov_zer(arr)
print(arr)
        