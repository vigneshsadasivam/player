n=int(input())
a=list(map(int,input("enter").split(" ")))[:n]
c=0
for i in range(1,len(a)):
  c=c+a[i]+a[i-1]
print(c)
