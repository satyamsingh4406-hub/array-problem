def duplicate(arr):
    n=len(arr)
    lis=[]
    dupl=set()
    for i in range(n):
        if arr[i] in lis:
            dupl.add(arr[i])
        else:
            lis.append(arr[i])
    print(dupl)

arr=[1,2,1,1,3,4,6,3]
duplicate(arr)