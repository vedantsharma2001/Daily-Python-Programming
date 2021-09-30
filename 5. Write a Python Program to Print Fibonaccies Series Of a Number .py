a=0
b=1
store=[a,b]
for i in range(0,10):
    c=a+b
    a=b
    b=c
    store.append(b)
print(store)