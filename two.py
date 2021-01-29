def fun(dict2,n):
    m=0
    k=0
    for i in range(1,n+1):
        if m < int(dict2[i]):
            k=i
            m=int (dict2[i])
    d={k:m}
    return d
dict1={}
dict2={}
n=int(input("Enter How many Students "))
for i in range(1,n+1):
    dict1[i]=input("Enter UserName ")
    dict2[i]=input("Enter ExamScore ")
print(fun(dict2,n))