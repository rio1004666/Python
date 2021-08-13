"""
날짜 : 2021/08/13
이름 : 강병화
내용 : 파이썬 팩토리얼 함수 문제
"""

def factorial(n): # 자기 자신을 부른다 반복문이 된다 recursive => 잘안쓴다 위험하다 종료조건 반드시 붙여야하고 방대해질수록 스택증가


    if n <= 1:

        return 1

    return n * factorial(n-1)

if __name__ == '__main__':

    print('3!:', factorial(3))
    print('4!:', factorial(4))
    print('5!:', factorial(5))
