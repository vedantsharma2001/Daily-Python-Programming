n=list(map(int,input("Enter the integers:").split(",")))
b=set(n)
length=len(n)
if(len(n)==len(b)):
    print("All Unique")
else:
    print("Duplicate")
