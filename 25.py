a=int(input("enter a numbers"))
l=[]
for i in range(0,a):
    b=input("enter string")
    l.append(b)
l.sort(key=len)
print(" ".join(l))
