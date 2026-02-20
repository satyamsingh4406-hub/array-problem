def freq(arr):
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

arr=[1,2,3,2,1,32,423,423]
print(freq(arr))

