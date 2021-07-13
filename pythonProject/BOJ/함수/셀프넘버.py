a=set()
num=set(range(1,10001))
for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    a.add(i)
b=sorted(num-a)
for k in b:
    print(k)