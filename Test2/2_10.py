import random

def game():
    word = ['가위','바위','qh']
    while True:
        you_word = input('가위, 바위, 보 입력: ')
        try:
            if you_word not in word:
                raise ValueError
        except ValueError:
                print('잘못 입력 하셨습니다.')
           continue
        else:
            break
