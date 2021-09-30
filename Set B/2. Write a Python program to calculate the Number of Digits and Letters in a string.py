main_string=input("Enter the string:")
final_string=""
d=0
l=0
for i in main_string:
    if i.isdigit():
        d=d+1
    if i.isalpha():
        l=l+1
print("Digits:",d,"Letters:",l)