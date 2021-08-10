"""
날짜 : 2021/08/10
이름 : 강병화
내용 : 파이썬 자료구조 Tuple 실습하기 교재 p92
"""

#Tuple(고정 리스트)
tuple1 = (1, 2, 3, 4, 5)
print('tuple1 type: ', type(tuple1))
print('tuple1 : ', tuple1)
print('tuple1[0]:', tuple1[0])
print('tuple1[1]:', tuple1[1])
print('tuple1[2]:', tuple1[2])

tuple2 = ('서울','대전','대구','부산')



tuple3 = 1, 2, 3, 4, 5  #()생략가능하다

#tuple3[0] = 7  수정시도하려면 에러

print('tuple3:', tuple3)