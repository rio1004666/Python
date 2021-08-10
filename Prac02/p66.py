numData = []
while True:
    num = int(input('숫자입력: '))
    if num % 10 == 0: # 내가 입력한 값이 10의 배수이면 종료
        print('프로그램 종료')
        break
    else:
        print(num)
        numData.append(num)

