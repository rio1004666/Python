"""
날짜 : 2021/08/13
이름 : 강병화
내용 : 파이썬 리스트에 점수를 입력하고 리스트 총합을 구하기
"""

scores = []
while True:
    print('0:종료','1:입력')
    result = int(input('입력: '))
    if result == 0:
        break
    score = int(input('점수입력: '))
    scores.append(score)
print('입력한 점수 확인')
print(scores)

sum1 = 0
sum2 = 0
for score in scores:
    sum1 += score
sum2 = sum(scores)
print('리스트 총합: ', sum1)
print('리스트 총합: ', sum2)