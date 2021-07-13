result=[]
def solution(lottos, win_nums):
    sum=0
    num=0
    for i in range(len(lottos)):
        if lottos[i]==0:
            sum+=1
        elif lottos[i] in win_nums:
            num+=1
    for j in range(2):
        if sum+num==6:
            result.append(1)
        elif sum_num==5:
            result.append(2)
        elif sum_num == 4:
            result.append(3)
        elif sum_num==3:
            result.append(4)
        elif sum_num == 2:
            result.append(5)
        else:
            result.append(6)
    print(result)