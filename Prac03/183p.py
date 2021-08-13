

from Prac03.Rectangle import Rectangle
print('사각형의 넓이와 둘레를 계산합니다.')
w = int(input('사각형의 가로 입력: '))
h = int(input('사각형의 세로 입력: '))

rec = Rectangle(w, h)
area = rec.area_calc()
circum = rec.circum_calc()
print('사각형의 넓이: ', area)
print('사각형의 둘레: ', circum)

