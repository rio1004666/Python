class Account:

    def __init__(self,bank,id,name,balance):
        # 속성
        # __가 접근제어함 외부에서 직접 참조하지 못하게하는 캡슐화
        self._bank = bank
        self._id = id
        self._name = name
        self._balance = balance

    def deposit(self, money):
        self._balance += money

    def withdraw(self, money):
        self._balance -= money

    def show(self):

    #기능
        print('은행명:', self._bank)
        print('계좌번호:', self._id)
        print('입금주:', self._name)
        print('잔액조회:', self._balance)





