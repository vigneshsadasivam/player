n=input("enter string")
a=[]
b=[]
w=[]
c=['a','e','i','o','u']
for i in n:
  if i in c:
    a.append(i)
  else:
    b.append(i)
for i in a:
  w.append(i)
for i in b:
  w.append(i)
print("".join(str(x) for x in w))
