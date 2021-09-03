"""
날짜: 2021/09/03
이름: 강병화
내용: 코딩테스트 - 파이썬 정렬 라이브러리 실습
"""

array = [5,7,9,0,3,1,6,2,4,8]
# sorted: 퀵정렬 알고리즘을 기반으로 설계된 파이썬 정렬 함수

result1 = sorted(array)
print('result1:', result1)
result2 = sorted(array, reverse=True)
print('result: ', result2)

# 파이썬 리스트 정렬 멤버함수

array.sort()
print('array1: ', array)
array.sort(reverse=True)
print('array2: ', array)


# key 매개변수의 활용

dataset = [['바나나',2],['사과',5],['당근',3]]
def setting(data):
    return data[1]
# 각 리스트의 두번째 값을 기준으로 정렬할것이다
ds1 = sorted(dataset,key=setting)
print('ds1 : ', ds1)
ds2 = sorted(dataset,key=lambda data: data[1])
print('ds2: ', ds2)