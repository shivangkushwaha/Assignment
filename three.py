def output(l,n):
    c=1
    count=[]
    for i in range(0,n-1):
        if l[i]==l[i+1]:
            c=c+1
        else:
            count.append(c)
            c=1
    print(count)
    return max(count) 
n=int(input("Enter Number Of Elements:"))
l=[]
for i in range(n):
    l.append(int(input("Enter Number: ")))
print(output(l,n))