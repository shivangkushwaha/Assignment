def sum(l):
    s=0
    for i in l:
        s+=i
    return s
l=[]
n=int(input("Enter How many Elements"))
for i in range(n):
    l.append(int(input("Enter an Integer")))
print("Sum=",sum(l))

