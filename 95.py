n,p,k=map(int,input("enter number").split(" "))
n=str(n)
a=[]
for i in n:
  a.append(i)
print(a[p+k-1])
