
"""

 날짜: 2021/08/11
 이름: 강병화
 내용: 파이썬 내장함수 실습하기 교재 p118

"""

# 패키지 모듈
import time # 시간
import math # 수학
import random   #임의의수

# time ####################################################
t1 = time.time() # Unix time
print('t1: ', t1)
t2 = time.ctime() #변환된 unix time
print('t2:', t2)

now = time.localtime(time.time()) # now객체를 만듬 개별적인 시간 구함

year = time.strftime('%Y', now)
month = time.strftime('%m', now)
date = time.strftime('%d', now)
hour = time.strftime('%H', now)
min = time.strftime('%M', now)
sec = time.strftime('%S', now)

print('%s년 %s월 %s일' % (year, month, date))
print('{}시 {}분 {}초'.format(hour, min, sec))


# math ###########################################################

r1 = abs(-5)

print('r1:', r1)

# ceil : 무조건 올림

r1 = math.ceil(1.2)
r2 = math.ceil(1.9)
print('r1:', r1)
print('r2:', r2)

# floor : 내림
r4 = math.floor(1.2)
r5 = math.floor(1.8)

print('r4:', r4)
print('r5:', r5)


# round : 반올림

r6 = round(1.2)
r7 = round(1.8)
print('r6:', r6)
print('r7:', r7)


# random ##############################################################

num1 = random.random()
print('rand1: ', num1) # 0 ~ 1 사이 임의의 실수
num2 = num1 * 10
print('rand2: ', num2)
num3 = math.ceil(num2)
print('rand3:', num3)

result = math.ceil( random.random() * 45 )
print('result: ', result)
########################################################################

