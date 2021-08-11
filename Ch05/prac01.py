import builtins
print(dir(builtins))
# builtins에서 제공하는 주요 내장함수 =>  import 할 필요 없는 함수들
print(abs(-444)) # 절댓값

dataset = set(range(1, 6))
datalist = [i for i in range(1, 6)]
datalist2 = list(map(str, str(1111111)))

# list   내장 클래스는  반복이가능한것들은 모두 list가능하다!!!!   iterable!!

# map    내장함수는 문자열 즉 반복가능한 문자의 배열이고 어떤 함수를 거쳐서 적용해서 list를 만든다

# str 내장 클래스는 대상 객체를 문자열로 전환시킨다 그걸 map에서 하나씩 str클래스로 다시 적용해서 리스트로 반환한다
print(datalist2)


print('dataset:', dataset)
print('datalist:', datalist)

print('set_len: %d' % len(dataset)) # len 도 builtins 모듈의 내장함수 import없이 바로 사용 가능
print('list_len: {0}'.format(len(datalist)))  # print도 builtins 모듈의 내장함수   format도 내장함수
print('set_sum: %d' % sum(dataset))
print('list_sum: {}'.format(sum(datalist)))
print('set_max: %d' % max(dataset))
print('list_max: {}'.format(max(datalist)))
print('set_min: %d' % min(dataset))
print('list_min: {}'.format(min(datalist)))


# eval 문자열 수식을 인수로 받아서 계산 가능한 파이썬 수식으로 변환
flag1 = all([3,4,True,False,'343','홍길동']) # 리스트안에 다양한 타입이 들어갈 수 있다 0이 아닌수는 True로 인식 0은 False로 인식
flag2 = all([3,4]) # 0이 아닌수는 가 True
flag3 = all([3,0,4]) # 0은 False로 인식하므로 False가 반환
flag4 = any([3,4,5,0]) # 어느 하나라도 True면 True반환
print('all 내장함수: {0}'.format(flag3))
print('any 내장함수: {0}'.format(flag4))

print('10진수를 2진수로 변환 bin()내장함수: ',bin(10)) # 10진수를 2진수로 변환

x = [i for i in range(1,6)]
print(dir(x)) # 해당 객체의 변수 내장함수 내장클래스 목록을 반환
print(hex(10)) # 해당 10진수를 16진수로 반환한다 Ox로 시작 2진수는 Ob로 시작
print(oct(10)) # 해당 10진수를 8진수로 반환한다 Oo로 시작한다 8진수는
print('a의 아스키코드값: %s' % ord('a')) # 해당 문자의 아스키코드값 반환
print('A의 아스키코드값: {}'.format(ord('A')))
print('2의 3승은: %d' % pow(2,3))


print(eval('40+30'))

