try:
    score=[3,4,6,17,19,23,30]
    print(score.index(10))
except ValueError:
    print("찾으시는 값이 없습니다. ",ValueError)
else:
    print("score안에 찾으시는 값이 있습니다")
finally:
    print("수고하셨습니다.")

# try:
#     c = divide(5, 0)
# except ZeroDivisionError:
#     print("두번째 인자가 0이어서는 안된다.")
# except TypeError:
#     print("[에러] {} {}모든 인자는 숫자여야 합니다.".format(5,'string'))
# except Exception as e:
#     print("에러 발생 : ", e)
# else:
#     print("결과 값은 {}".format(c))
# finally:
#     print("프로그램 실행이 완료되었습니다.")