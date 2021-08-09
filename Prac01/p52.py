
#특정 문자 갯수

oneLine = 'this is one line string'
print('t 글자수: ', oneLine.count('t'))

#접두어

print(oneLine.startswith('this'))
print(oneLine.startswith('that'))


#문자열 교체

print(oneLine.replace('this', 'that'))