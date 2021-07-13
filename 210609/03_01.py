# try:
#     fruits=['사과','포도','바나나']
#     print(fruits[4])
# except IndexError:
#     print("에러 발생",IndexError)
#
# ##실습)리스트 작성. 인덱스 에러 발생시킴
# try:
#     subject=["수학","국어","영어","과학"]
#     print(subject[4])
# except IndexError:
#     print("에러 발생",IndexError)

try:
    a = 30
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("0으로 나누기 에러 발생",ZeroDivisionError)