class CalFnc2:
    def __init__(self, result, color):
        self.result = result
        self.col = color
    def plus(self, num):
        self.result += num
        return self.result
    def sub(self, num):
        self.result -= num
        return self.result
a1 = CalFnc2(3, 'blue')  # 계산기 한대
a2 = CalFnc2(3, 'black')  # 계산기 한대
a3 = CalFnc2(3, 'orange')  # 계산기 한대
print(a1.col)
print(a2.col)
print(a3.col)