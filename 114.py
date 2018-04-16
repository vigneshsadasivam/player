a=int(input("enter number"))
s=0
while(a>0):
  n=a%10
  s=s+(n*n)
  a=a//10
print(s)
