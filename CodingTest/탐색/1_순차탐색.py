"""
날짜: 2021/09/17
이름: 홍길동
내용: 코딩테스트 - 순차탐색
"""
def sequential_search(dataset, target):

    pos = -1

    for i in range(len(dataset)):
        if dataset[i] == target:
            pos = i
    return pos

dataset = [5, 10, 18, 22, 35, 55, 75, 103, 152]

value = int(input('검색할 숫자: '))

pos = sequential_search(dataset,value)

if pos == -1:

    print('찾으시려는 숫자가 없습니다.')

else:

    print('찾으시려는 숫자는: ', pos)