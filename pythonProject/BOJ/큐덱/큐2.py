import sys
num=int(input())
q=[]
for i in range(num):
    cal=sys.stdin.readline().split()
    if cal[0]=='push':
        q.append(int(cal[1]))
    elif cal[0]=='pop':
        if len(q)==0:
            print(-1)
        else:
            print(q.pop(0))
    elif cal[0]=='size':
        print(len(q))
    elif cal[0]=='empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif cal[0]=='front':
        if len(q)!=0:
            print(q[0])
        else:
            print(1)
    elif cal[0]=='back':
        if len(q)!=0:
            print(q[-1])
        else:
            print(-1)

