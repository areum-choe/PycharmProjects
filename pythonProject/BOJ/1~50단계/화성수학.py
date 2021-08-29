num=int(input())

for i in range(num):
    a=list(map(str,input().split()))
    answer=float(a[0])
    for j in range(len(a)):
        if a[j]=="@":
            answer*=3
        elif a[j]=="%":
            answer+=5
        elif a[j]=="#":
            answer-=7
    print('%.2f'%answer)