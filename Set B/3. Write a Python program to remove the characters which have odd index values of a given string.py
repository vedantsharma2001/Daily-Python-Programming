main_string=input("Enter the string:")
final_string=""
for i in range(len(main_string)):
    if i % 2 == 0:
        final_string=final_string+main_string[i]
print(final_string)

                  OR


a=input("Enter the string:")
b=a[1::2]
print(b)