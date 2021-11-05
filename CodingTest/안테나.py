"""
날짜: 2021/11/05
이름: 강병화
내용: 정렬
"""
N = int(input())
houses = list(map(int,input().split()))

houses.sort()

result = houses[(N-1) // 2]
print(result)