"""

날짜 : 2021/08/09
이름 : 강병화
내용 : 파이썬 문자열 실습하기 교재 p48

"""

#문자열 더하기
str1 = 'hello'
str2 = 'Korea'
str3 = str1 + str2
print('str3: ', str3)

#문자열 곱하기

message = 'hello'

result = message * 3

print('result: ', result)

#문자열 길이

sample = 'Hello World'
print('sample 길이: ', len(sample))


#문자열 인덱스

print('sample 1번째 문자: ', sample[0])
print('sample 7번째 문자: ', sample[6])
print('sample -1번째 문자: ', sample[-1])




#문자열 자르기

print('sample 0 ~ 5까지 문자열: ', sample[0:5])
print('sample 0 ~ 5까지 문자열: ', sample[:5])
print('sample 6 ~ 11까지 문자열: ', sample[6:11])
print('sample 6 ~ 마지막까지 문자열: ', sample[6:])


#문자열 분리


people = '김유신^김춘추^장보고^강감찬^이순신'

p1, p2, p3, p4, p5 = people.split('^');

print('p1:', p1)
print('p2:', p2)
print('p3:', p3)
print('p4:', p4)
print('p5:', p5)

#문자열 이스케이프(회피하다)

print('안녕!\n 파이썬!') # 개행 = 줄바꿈
print('안녕!\t 파이썬!') # 탭 = 들여쓰기
print('안녕!\b 파이썬!') # backspace = 지우기
# '' 나 "" 는 문자열을 감싸는 기능을 가진 특수문자이기때문에
# 실제 '' 나 "" 를 출력하기 위해서는 이스케이프해주어야한다
print("안녕! '파이썬'") # 그것을 피하기위해 "" 와 ''가 구분되어서 바깥에는 ""를 문자열로 처리하는 특수문자로 하고''를 안에서 실제로 구현해준다
print("안녕! \"파이썬\"")  # 하지만 또 쌍따옴표를 사용하기 위해서 쌍따옴표는 이스케이프해줘야한다



