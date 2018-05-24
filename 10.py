a,b=input().split(' ')
c=0
f=len(a)
for i in range(f):
  if(a[i]!=b[i]):
    c=c+1
if(c==1):
  print("yes")
else:
  print("no")
