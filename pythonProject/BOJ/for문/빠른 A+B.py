import sys

inp=int(input())
for i in range(inp):
    a,b,c=map(int,sys.stdin.readline().split())
    # a = map(int, sys.stdin.readline().split())
    # b = map(int, sys.stdin.readline().split())
    #print(sep='\n')
    print(a+b+c)