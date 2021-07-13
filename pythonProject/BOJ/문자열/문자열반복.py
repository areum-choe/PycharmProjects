num=int(input())

for i in range(num):
    n,l=input().split()
    a=""
    for j in l:
        a+=j*int(n)
    print(a)