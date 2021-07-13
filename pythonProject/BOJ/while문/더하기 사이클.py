a=int(input())
i=0
b=a
while True:
    ten=a//10
    one=a%10
    i+=1
    a=((ten+one)%10)+one*10
    if b==a:
        break
print(i)