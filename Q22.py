def all_sub(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n): 
            print(arr[i:j+1])

arr=[1,2,3,4]
all_sub(arr)