def missing(arr):
    lis=list(range(1,50))
    for i in lis:
        if i not in arr:
            return i
        
arr=[-2,-5,-6,1,2,4,5,8]
print(missing(arr))