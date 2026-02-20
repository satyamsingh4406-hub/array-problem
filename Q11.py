def remov(arr,ele):
    lis=[]
    for i in arr:
        if(i!=ele):
            lis.append(i)
    return lis

arr=[1,2,3,4,5,4,7,4,8,4]
n=int(input("Enter The Number: "))
print(remov(arr,n))