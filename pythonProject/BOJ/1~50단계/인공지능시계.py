a,b,c=map(int,input().split())
d=int(input())

if c+d>=60:
    b+=(c+d)//60
    e=(c+d)%60
    if b>=60:
        a+=b//60
        b=b%60
        if a>23:
            a-=24
else:
    e=c+d
print(a,b,e)