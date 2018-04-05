a=int(input("enter start"))
b=int(input("enter end"))
s=0
for i in range(a,b+1):
  if(i%2!=0):
    s=s+i
print(s)
