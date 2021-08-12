"""
날짜: 2021/08/12
이름: 강병화
내용: 파이썬 캡슐화 실습하기 교재 p161
"""

from Ch06.sub1.Account import Account

kb = Account('국민은행','101-101-1001','김유신',10000)

kb.deposit(4000)
kb.withdraw(5000)
# 접근제어 은폐하면 직접참조 불가

# 캡슐화(정보은닉)을 적용해서 취약코드 예방
# kb.balance -= 1    #직접 접근하면 위험한 코드

kb.show()