def equal(arr,brr):
    n=len(arr)
    m=len(brr)
    if(n!=m):
        return False
    for i in arr:
            if i not in brr:
                 return False
    return True

arr=[3,4,5,6,7,1]
brr=[1,6,4,4,5,3]
ans=equal(arr,brr)
print(ans)