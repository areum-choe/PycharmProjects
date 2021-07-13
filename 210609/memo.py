import sys

try:
    option = sys.argv[1]
except IndexError:
    print("파일의 추가 정보-모드를 입력해 주세요. (-r, -w, -a)")
    option = ''


if len(sys.argv) < 2:
    print("추가 정보가 없습니다.")
    option = ''

if option == '-a':
    memo=sys.argv[2]
    f=open('memo.txt','a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option =='-r':
    f=open('memo.txt','r')
    memo=f.read()
    f.close()
    print(memo)
elif option == '-w':
    memo=sys.argv[2]
    f=open('memo.txt','w')
    f.write(memo)
    f.write('\n')
    f.close()