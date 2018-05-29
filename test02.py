
no = input('숫자 5개를 , 로 구분하여 입력하세요 : ')
result = no.split(',')

sum = 0

for i in result :

    sum += int(i)


avg = sum/5

print('평균은 %3.1f 입니다'% avg)