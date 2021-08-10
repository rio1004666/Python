var = 10
if var <= 5:
    print('var=', var)
    print('var는 5보다 크다.')
    print('조건이 참인 경우 실행')

print('항상실행')
score = int(input('점수 입력:'))
if score >= 85 and score <= 100:
    print('우수')
else:
    if score >= 70:
        print('보통')
    else:
        print('저조')

score2 = int(input('점수 입력: '))
grade = ''
if score >= 85 and score <= 100:
    grade = '우수'
elif score >= 70:
    grade = '보통'
else:
    grade = '저조'
print('당신의 점수는 %d이고 등급은 %s 입니다' % (score, grade))
print('당신의 점수는 {} 이고 등급은 {} 입니다.'.format(score, grade))
print('당신의 점수는 ',score, '이고, ', '등급은 ', grade, ' 입니다.')
num = 9
result = 0
if num >= 5:
    result = num + 2
else:
    result = num + 2
result2 = num * 2 if num >= 5 else num + 2



