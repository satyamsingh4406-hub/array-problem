def missing(arr,n):
    lis=list(range(1,n+1))
    for i in lis:
        if i not in arr:
            print("The missing number is:",i)

arr=[1,2,4,5,7,8]
n=int(input("Enter The Range"))
missing(arr,n)
