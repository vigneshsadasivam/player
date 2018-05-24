import math
i,r=list(map(int,input("").split(' ')))
c=0
for i in range(i,r+1):
  a=math.sqrt(i)
  if(a==int(a)):
    c=c+1
print(c)
