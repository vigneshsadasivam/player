l,r=map(int,input("enter l,r").split(" "))
if(l>r):
  a=l
else:
  a=r
for i in range(a,100000):
  if(i%l==0 and i%r==0):
    print(i)
    break
  
