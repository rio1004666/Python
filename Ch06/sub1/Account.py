class Account:

    def __init__(self,bank,id,name,balance):
        # 속성
        self.bank = bank
        self.id = id
        self.name = name
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money

    def show(self):

    #기능
        print('은행명:', self.bank)
        print('계좌번호:', self.id)
        print('입금주:', self.name)
        print('잔액조회:', self.balance)
