def freq(arr):
    n=len(arr)
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        if d[i]>n//2:
            return d

arr=[1,1,1,1,2,3,4]
print(freq(arr))    
    