esc = True
account = 0

while esc:

    print('-'*30)
    print('1.예금 | 2.출금 | 3.잔고 | 4.종료')
    print('-'*30)
    no = int(input('선택>'))

    if no == 1 :
        account += int(input('예금액>'))

    elif no == 2 :
        account -= int(input('출금액>'))

    elif no == 3 :
        print('잔고액>', account)
    elif no == 4 :
        print('프로그램 종료')
        esc = False
    else:
        print('다시 입력해주세요')




