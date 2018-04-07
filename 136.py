n,k=map(int,input("enter n k").split(" "))
a=[]
for i in range(0,n):
  b=int(input())
  a.append(b)
if k in a:
  print("yes",a.count(k))
else:
  print("no")
