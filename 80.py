n=int(input("enter n"))
a=[]
for i in range(0,n):
  b=int(input())
  a.append(b)
a.sort()
print(a[1]-a[0])
