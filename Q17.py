def leader(arr):
    s=0
    e=len(arr)-1
    while(s<e):
        mid=(s+e)//2
        if(arr[mid]<arr[mid+1]):
            s=mid+1
        else:
            e=mid
    return(arr[e])

arr=[3,4,5,0,1,2]
print(leader(arr))

