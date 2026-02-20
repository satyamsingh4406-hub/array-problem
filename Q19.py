def sub_arr(arr,tar):
    n=len(arr)
    Sum=s=0
    for i in range(n):
        Sum+=arr[i]
        while(Sum>tar):
            Sum-=arr[s]
            s+=1
        if(Sum==tar):
            return s,i
        
    return False

arr=[1,2,3,4,5,6,7,8]
print(sub_arr(arr,7))
