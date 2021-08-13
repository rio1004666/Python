"""
날짜 : 2021/08/13
이름 : 강병화
내용 : 파이썬 정규 표현식 연습문제
"""
from re import findall, sub # 정규표현식을 사용하는 메서드들을 가져오는데 필요한 모듈을 import re

texts_re1 = ['abc동해물과 123백두산이 eefa마르고 456닳도록789',
             '^하느님이 보우하사!@#$ 우리나라 만세&&']
print('texts_re1: ', texts_re1)
#숫자제거

texts_re2 = [sub('[0-9]','',text) for text in texts_re1] # 리스트에서 하나씩 꺼내서 어떤 작업을 거치도록하고 다시 리스트로 변환
print('texts_re2:',texts_re2)
# 자바에서는 스트림이다
# map 내장함수 사용
#특수문자 제거
texts_re3 = [sub("[!@#$%^&*()]",'',text) for text in texts_re2]
print('texts_re3:',texts_re3)
#영문자 제거
texts_re4 = [sub("[a-z][A-Z]",'',text) for text in texts_re3]
print('texts_re3:',texts_re4)