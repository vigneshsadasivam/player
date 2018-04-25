def fact(a):
  b=1
  for i in range(1,a+1):
    b=b*i
  return(b)
a,b=map(int,input("enter a b").split(" "))
print(fact(a)//fact(b))
