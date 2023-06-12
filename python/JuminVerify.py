jumin = input('주민등록번호 : ')
jumin = '821010-1635214'
# print(jumin)

# phase 1
first = int(jumin[0])*2 + int(jumin[1])*3 + int(jumin[2])*4 +\
        int(jumin[3])*5 + int(jumin[4])*6 + int(jumin[5])*7 +\
        int(jumin[7])*8 + int(jumin[8])*9 + int(jumin[9])*2 +\
        int(jumin[10])*3 + int(jumin[11])*4 + int(jumin[12])*5
#print(first)

# phase 2
second  = first % 11
# print(second)

# phase 3
third = 11 - second

# phase 4
if third == int(jumin[13]):
  print('[ OK ] 유효한 주민번호입니다.')
else:
  print('[ Fail ] 유효하지 않은 주민번호입니다.')