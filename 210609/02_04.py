class CalFnc3:
    def __init__(self, result):
        self.result = result
    def plus(self, num):
        self.result += num
        return self.result
    def sub(self, num):
        self.result -= num
        return self.result
    def mul(self,num):
        self.result **=num
        return self.result
    def div(self, num):
        self.result /= num
        return self.result

class CalFnc3_change(CalFnc3):  # CalFnc3를 상속받음
    def __init__(self, result):
        self.result = result

    def div(self, num):
        if num == 0:
            return 0
        else:
            self.result /= num
        return self.result

a = CalFnc3_change(0)
tmp = a.plus(5)
tmp1 = a.div(0)
print(tmp1)

## CalFnc3 mul메소드를 추가하고, 새로운 클래스를 만들고(상속)받아서
## 이를 실행시켜보자.(3대 계산기)
class CalFnc3_change1(CalFnc3):  # CalFnc3를 상속받음
    def __init__(self, result=0):
        self.result = result

    def div(self, num):
        if num == 0:
            return 0
        else:
            self.result /= num
        return self.result

b1=CalFnc3_change1(0)
print(b1.mul(10))