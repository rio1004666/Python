"""


날짜 : 2021/08/10
이름 : 강병화
내용 : 파이썬 자료구조 List 실습하기 교재 p60


"""

#list 파이썬에서는 배열이 없삿!!!!!

list1 = [1, 2, 3, 4, 5] # 선형 구조

print('list1 type: ', type(list1))
print('list1[0]: ', list1[0])
print('list1[1]: ', list1[1])
print('list1[2]: ', list1[2])
print('list1[3]: ', list1[3])
print('list1[4]: ', list1[4])
list2 = [5, 3.14, True, 'Apple'] # 다른 타입이 들어 갈 수 있다!!!!!

print('list2 type: ', type(list2))
print('list2[1] ', list2[1])
print('list2[2] ', list2[2])
print('list2[3] ', list2[3])
# 2차원 list 구조
list3 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
print('list3 type: ', type(list3))
print('list3[0][0]: ', list3[0][0])
print('list3[1][1]: ', list3[1][1])
print('list3[2][2]: ', list3[2][2])

#list 덧셈


ani1 = ['사자', '호랑이', '곰']
ani2 = ['코끼리', '기린']
ani3 = ani1 + ani2
print('ani3:', ani3)


#list 수정, 삭제


nums = [1, 2, 3, 4, 5]

nums[1] = 7

print('nums: ', nums)

nums[2:4] = [8, 9, 10] # 2인덱스부터 3인덱스까지 값을 변경 # 리스트를 통으로 넣을 수 있다.
print('nums: ', nums)
nums[3:5] = [] # 비워버린다
print('nums: ', nums)

#list 반복문

array = [1, 2, 3, 4, 5]
for n in array:
    print('n: ', n)
people = ['김유신', '김춘추', '장보고']
for person in people:
    print(person)
for i, value in enumerate(people): # 인덱스와 값 열거형 객체
    print('people[%d] : %s' % (i, value))

#list Comprehension  리스트 내포

numbers = [1, 2, 3, 4, 5]
res1 = [num * 3 for num in numbers] # 리스트안에 for문 가능
res2 = [num * 3 for num in numbers if num % 2 == 1] # 조건 추가 가능 (조건만족시 리스트에 데이터 추가 )
print('res1: {}'.format(res1))
print('res2: ', res2)