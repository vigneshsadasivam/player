a=int(input("enter a numbers"))
l=[]
m=[]
for i in range(0,a):
    b=input("enter string")
    l.append(b)
    m.append(b)
l.sort()
if(m==l):
  print("yes")
else:
  print("no")
