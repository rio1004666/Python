from statistics import mean
# #이름, 나이 , 생년월일 출력
# name = input("이름을 입력하시오: ")
# age = int(input("나이를 입력하시오: "))#입력받는 데이터는 항상 문자열이므로 캐스팅
# year = 2021 - age # 태어난 년도
# print(name, '님은 ', age, '세이고, ', year, ' 년도에 태어났습니다.') # \'을 사용하지않고 문자열을 쭉출력하면서 변수값을 넣고싶다면 '+변수명+'을 넣어준다
n1 = int(input("숫자1 입력하시오: "))
n2 = int(input("숫자2 입력하시오: "))
n3 = int(input("숫자3 입력하시오: "))

avg = float(mean([n1,n2,n3]))
print('평균은: ', avg)