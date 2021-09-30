n=int(input("Enter the number:"))
store=[2]
for i in range(2,n+1):
    if (i % 2) != 0:
        store.append(i)
print(store)