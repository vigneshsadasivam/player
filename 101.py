n=int(input("enter n"))
a=[]
c=0
for i in range(0,n):
  b=int(input())
  a.append(b)
for i in range(1,n):
  if(a[i]<a[i-1]):
    c=c+a[i-1]
  else:
    c=c+a[i]
print(c)
