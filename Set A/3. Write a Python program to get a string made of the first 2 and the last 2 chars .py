a=input("Enter the string 1:")
if(len(a)<2):
    print("Empty String")
else:
    print(a[0:2]+a[-2:])