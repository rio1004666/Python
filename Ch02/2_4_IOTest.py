"""

날짜 : 2021/08/09
이름 : 강병화
내용 : 파이썬 표준입출력 실습하기 교재 p38

"""
#파이썬 표준 입력 장치
num = input('숫자입력: ')

#파이썬 표준 출력 장치

print(num)
print('num type: ', type(num))

#그런데 입력받은 데이터타입은 문자열!!!!

#문자열을 숫자로 변환(캐스팅)

num = int(num) # 캐스팅

num += 1

print('+1한 결과 num:', num)

#출력 옵션

print('hello', end='~ ')
print('Busan~')
print('010', '1234', '5678', sep='-')

# 서식문자 출력

print('%d년 %d월 %d일 %s요일' % (2021, 8, 9, '월'))

#포맷문자 출력

print('이름:{}\n나이:{}\n주소:{}\n'.format('홍길동', 21, '부산광역시'))


#기본적으오 print 표준출력장치는 줄바꿈을 수행한다


print('hello', end=' ')
print('python')









