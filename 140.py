n=input("enter string")
a=len(n)
s=0
for i in n:
  if(i=="a"or i=="b"):
    s=s+1
if(s==a):
  print("s")
else:
  print("no")
    
