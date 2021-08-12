"""

날짜: 2021/08/12
이름: 강병화
내용: 파이썬 상속 실습하기 교재 p163

"""

from Ch06.sub1.StockAccount import StockAccount

#상속관계에서 부모멤버변수가 private이면 자식이 접근을 못하므로 접근하기위해 protected로 해준다 그냥 _이다
kb = StockAccount('KB중권','101-121-1010','김유신',30000,'삼성전자',1,80000)
kb.deposit(70000)
kb.withdraw(5000)
kb.show()

kb.sell(1, 80000)

kb.show()