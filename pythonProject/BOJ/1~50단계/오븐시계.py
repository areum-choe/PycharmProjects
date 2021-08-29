a,b=map(int,input().split())
c=int(input())


if b+c>=60:
    d=(b+c)%60
    a+=(b+c)//60
    if a>23:
        a-=24
else:
    d=b+c
print(a,d)
