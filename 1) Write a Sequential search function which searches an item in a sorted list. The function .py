a=list(map(int,input("Enter the numbers:").split(" ")))
a.sort()
b=int(input("Enter the number to be searched:"))
if b in a:
    print(a.index(b))
    print(a)