"""
날짜: 2021/09/17
이름: 강병화
내용: 코딩테스트 - 이진탐색 라이브러리 함수 실습
"""
from bisect import bisect_left,bisect_right
# 존재하지 않는 수를 찾으려고 할때는 그 수가 들어갈 위치값이다
dataset = [5, 10, 18, 22, 35, 55, 75, 103, 152]


def BinarySearch(dataset, target):
    i = bisect_left(dataset, target)
    if dataset[i] == target:
        return i
    else:
        return -1
value = int(input('검색할 숫자: '))
#pos = bisect_left(dataset, value)
pos = BinarySearch(dataset,value)
print('pos: ', pos)

# 해당되는 값을 찾지 못했을 경우 -1반환하게 해준다

