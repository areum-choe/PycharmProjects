a=int(input())
for i in range(a):
    b=input()
    c=0
    d=0
    for j in range(len(b)):
        if b[j]=='O':
            c+=1
            d+=c
        else:
            c=0
    print(d)


