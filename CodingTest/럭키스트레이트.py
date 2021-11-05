"""
날짜: 2021/11/05
이름: 강병화
내용: 코딩테스트 구현 - 럭키스트레이트
"""
n = input()
str_list = list(n)
mid_index = len(str_list) // 2
leftsum,rightsum = 0, 0
for i,s in enumerate(0,str_list):
    temp_s = int(s)
    if i < mid_index:
        leftsum += temp_s
    else:
        rightsum += temp_s
if leftsum == rightsum:
    print('LUCKY')
else:
    print('READY')