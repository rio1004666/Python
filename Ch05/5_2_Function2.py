
"""

 날짜: 2021/08/11
 이름: 강병화
 내용: 파이썬 함수 실습하기 교재 p88

"""
# 디폴트 매개변수
def hello(name='홍길동',age=21):
    print('이름:', name)
    print('나이:', age)


hello()
hello('이순신')
hello('김춘추', 44)

# 가변 매개변수
def total(*scores):
    tot = 0
    for score in scores:
        tot += score
    return tot
# 매개변수를 마음대로 넣을 수 있다  -> 리스트로 들어간다
r1 = total(1, 2, 3)
r2 = total(1, 2, 3, 4, 5, 6)
r3 = total(1, 2, 3, 4, 5, 6, 7, 8)

print('r1: ', r1)
print('r2: ', r2)
print('r3: ', r3)

# 하나 이상의 리턴값 일반적인 리턴값은 하나뿐
def plus_multi(num1,num2):
    y1 = num1 + num2
    y2 = num1 * num2
    return y1, y2

res1, res2 = plus_multi(3, 5)

print('res1: {0} res2: {1}'.format(res1, res2))

#  변수에 저장하는 함수

def plus(x,y):
    return x+y

def minus(x,y):
    return x-y

#  함수 실행이아닌 변수에 저장
var1 = plus
res1 = var1(2,3)
var2 = minus
res2 = var2(3,4)
print('res1:', res1)
print('res3:', res2)

# 함수 리스트로 만들 수도 있다
funcs = [plus, minus]
res3 = funcs[0](1, 2)
res4 = funcs[1](214, 56)
