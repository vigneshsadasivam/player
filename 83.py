n=int(input("enter n"))
a=[]
for i in range(0,n):
  b=int(input())
  a.append(b)
s=a[0]
for i in a:
  s=s|i
print(s)
