# class Cal:
#     pass
# a=Cal()
# b=Cal()

result=0
def plus(num):
    global result
    result+=num
    return result
print(plus(3))
print(plus(4))