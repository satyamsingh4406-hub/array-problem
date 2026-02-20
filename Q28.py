def sor(arr):
    s=0
    mid=0
    e=len(arr)-1
    while(mid<=e):
        if(arr[mid]==0):
            arr[s],arr[mid]=arr[mid],arr[s]
            s+=1
            mid+=1
        elif(arr[mid]==1):
            mid+=1
        else:
            arr[mid],arr[e]=arr[e],arr[mid]
            e-=1
    return arr

arr=[0,1,2,1,2,0,2,1,0,2,1]
print(sor(arr))
