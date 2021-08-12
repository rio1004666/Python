

# 프로그래밍에서 반복되는 코드는 상당히 좋지않아서 상속이라는 개념 사용
# 기능을 받아서 사용!!!!! 반복 제거
from Ch06.sub1.Account import Account

class StockAccount(Account) : # 상속받음
    # 상속을 받으면 부모클래스의 변수들을 초기화해주어야함
    def __init__(self, bank, id, name, balance, stock, amount, price):

        super().__init__(bank, id, name, balance) #부모의 생성자에 있는 변수를 가져와서 같이 초기화한다
        self._stock = stock
        self._amount = amount
        self._price = price

    def sell(self, amount, price):

        self._balance += amount * price

    def buy(self, amount, price):

        self._balance -= amount * price

    def show(self):

        # 기능

        print('은행명:', self._bank)
        print('계좌번호:', self._id)
        print('입금주:', self._name)
        print('현재잔액:',self._balance)
        print('주식종목:', self._stock)
        print('주식수량:', self._amount)
        print('주식가격:', self._price)
        print('-------------------------')


