a=int(input("enter number"))
s=0
while(a>0):
  w=a%10
  s=s+(w*w)
  a=a//10
print(s)
