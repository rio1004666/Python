"""
날짜 : 2021/08/10
이름 : 강병화
내용 : 파이썬 자료구조 Set 실습하기 교재 p96
"""



# Set

set1 = {1, 2, 3, 4, 5, 3, 2} # set은 순서를 보장하지 않고 중복없는 키들의 모임
print('set1 type: ', type(set1))
print('set1: ', set1)


set2 = set('hello world') # 중복을 제거함 문자열에서 하나씩 뜯어서 set자료구조에 넣음
print('set2 type: ', type(set2))
print('set2: ',set2)
# 리스트 변환 후 출력
setTolist1 = list(set1) # 리스트 객체화
print('list1 : ', setTolist1)
print('list1[0] : ', setTolist1[0])
print('list1[1] : ', setTolist1[1])
print('list1[2] : ', setTolist1[2])


