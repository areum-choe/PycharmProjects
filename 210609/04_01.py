import mydream

print("모듈 불러오기 완료")

#모듈 안의 변수 사용하기
print(mydream.likecolor)

#모듈 함수
print("내가 좋아하는 색깔은:", mydream.likecolor)

me = mydream.myact()
print("힘들 때는 {} 그리고 마음껏 {}:".format(me.walk(), me.haha() ))