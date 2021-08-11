
"""

 날짜: 2021/08/11
 이름: 강병화
 내용: 파이썬 리스트 함수 실습하기 교재 p88

"""
import math

dataset = [1, 4, 3]

print('1-dataset: ', dataset)

dataset.append(2)
dataset.append(5)

print('2-dataset:', dataset)

# 데이터 정렬
dataset.sort()

print('sort() 결과: ', dataset)

dataset.sort(reverse=True)
print('desc sort() 결과:', dataset)
# 데이터 뒤집기
dataset.reverse()
print('dataset 역순: ', dataset)
#데이터 삽입
dataset.insert(2, 6)
print('리스트 삽입: ', dataset)

#데이터 삭제
dataset.remove(6)
print('dataset 삭제:',dataset)


#  map 함수 : 리스트의 데이터를 지정된 함수로 일괄 처리 해주는 함수

def plus10(n):
    return n + 10

list1 = [i for i in range(1,6)]
print('list1:', list1)
r1 = map(plus10, list1)
print('r1:', list(r1))
list2 = [0.1, 1.2, 2.6, 3.4, 4.9]
r2 = map(math.ceil,list2)
print('r2:', list(r2))

list3 = ['1','2','3','4','5']
r3 = map(int,list3)
print('r3: ', list(r3))