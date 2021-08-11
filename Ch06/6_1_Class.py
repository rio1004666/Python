
"""

 날짜: 2021/08/11
 이름: 강병화
 내용: 파이썬 객체지향 프로그래밍 실습하기 교재 p148

"""

# 자동차 클래스 정의
from Ch06.sub1.Account import Account
from Ch06.sub1.Car import Car

# from 에서는 경로 패키지와 모듈이름까지 모두 작성 후 import에서 모듈이름
# 객체 생성 => 사용이유 복잡한 나열뿐이 아닌 모듈화


bmw = Car('520d', '흰색', 5000) # new 연산자가 없다 객체 생성
bmw.speedUp()
bmw.speedDown()
bmw.show()
benz = Car('벤츠','검정색',7000)
benz.speedDown()
benz.speedUp()
benz.show()

kb = Account('국민은행','101-12-1111','김유신',10000)
kb.deposit(30000)
kb.withdraw(30000)
kb.show()

wr = Account('우리은행', '101-12-2222', '이순신', 70000)
wr.deposit(4000)
wr.withdraw(21000)
wr.show()