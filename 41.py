def is_power(n):
    n = n/k
    if n == k:
        print("s")
    elif n > k:
        return is_power(n)
    else:
        print("no") 
s=int(input("enter a number"))
k=int(input("enter k"))
is_power(s)
