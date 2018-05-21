s=input("enter word")
d=len(s)
g=s.count('a')+s.count('b')
if(d==g or d-g==1):
  print("yes")
else:
  print("no")
