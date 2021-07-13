a=int(input())

for _ in range(a):
    N=list(map(int,input().split()))
    avg=sum(N[1:])/N[0]
    count=0
    for j in N[1:]:
        if j>avg:
            count+=1
    per=(count/N[0])*100
    print('%.3f'%per+'%')






