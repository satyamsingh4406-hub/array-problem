def common(arr,brr):
    n=len(arr)
    m=len(brr)
    lis=[]
    for i in arr:
        for j in brr:
            if(i==j):
                lis.append(i)
    print(lis)

arr=[5,2,3,1,6]
brr=[7,2,5,1,65,32]
common(arr,brr)
