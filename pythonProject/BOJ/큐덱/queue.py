import sys
num=int(input())
q=[]
for i in range(num):
    cal=sys.stdin.readline().split()
    if cal[0]=='push':
        q.append(int(cal[-1]))
    elif len(q)==0:
        if cal[0]=='pop':
