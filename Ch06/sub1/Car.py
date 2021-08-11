
#모듈이라고 한다 클래스라고도 한다 폴더는 패키지라고 한다
class Car:
    def __init__(self, model, color, price):  # 생성자
        # 속성과 (데이터)
        # self는 클래스 자신을 가리킴 멤버
        self.model = model
        self.color = color
        self.price = price

    # 기능   (행위)
    def speedUp(self):
        print('%s speed Up...' % self.model)

    def speedDown(self):
        print('%s speed Down...' % self.model)

    def show(self):
        print('차량명:', self.model)
        print('차량색:', self.color)
        print('차량가격:', self.price)
