
"""

 날짜: 2021/08/11
 이름: 강병화
 내용: 파이썬 함수 실습하기 교재 p88

"""

# 함수 (일련의 로직을 재활용하기 위해 모듈화한 로직단위)

def f(x):
    y = 2 * x + 3
    return y

y1 = f(1)
y2 = f(2)
y3 = f(3)

print('y1:', y1)
print('y2:', y2)
print('y3:', y3)

# 타입1 - 매개변수 O , 리턴값 O
# 타입1 - 매개변수 O , 리턴값 X
# 타입1 - 매개변수 X , 리턴값 O
# 타입1 - 매개변수 X , 리턴값 X

def type1(x,y):
    z = x + y
    return z
r1 = type1(1,2)
r2 = type1(2,3)

print(r1)
print(r2)

def type2(items):
    tot = 0
    for item in items:
        tot += item
    print('총합: ', tot)

type2([1,2,3,4,5])


type2((4,56,6,3,2)) #튜플은 괄호 생략 가능 인자로는 안된다 가변인자로 된다
# 타입3 - 매개변수 X 리턴값 O
def type3():
    tot = 0
    for k in range(11):
        tot += k
    return tot

r3 = type3()

print('r3:', r3)
#타입4 - 매개변수 X 리턴값 X
def type4():
    print('type4(): ', type3())
type4()

# 연습문제
def gugudan(dan):
    print('%d단' % dan)
    for i in range(1, 10):
        print('{} x {} = {}'.format(dan, i, i*dan))

gugudan(2)
gugudan(4)
gugudan(7)