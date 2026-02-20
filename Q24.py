def rot(arr):
    arr.sort()
    s=0
    e=len(arr)-1
    lis=[]
    while(s<e):
        if(s!=e):
            lis.append(arr[s])
            lis.append(arr[e])
        else:
            lis.append(arr[s])
        s+=1
        e-=1
    return lis

arr=[1,3,5,2,4,7,10,9,8,6,2]
print(rot(arr))