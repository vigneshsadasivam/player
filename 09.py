a=int(input("enter start number"))
b=int(input("enter end number"))
c=0
for num in range(a,b+1):
  if num > 1:
    for i in range(2,num):
      if (num % i) == 0:
        break
    else:
        c=c+1
print(c)
