import re

data = '''
part 801122-1422351
lim  810111-1422352
lim1   222-14223
'''
p=re.compile("(\d{6})[-]\d{7}")
print(p.sub("\g<1>-*******",data))