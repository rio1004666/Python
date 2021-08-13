"""
날짜 : 2021/08/13
이름 : 강병화
내용 : 파이썬 로또 번호 생성 문제
"""

import math, random

def lotto():
    lotto_set = set() # 중복을 제거하기 위한 set자료구조
    #lotto_set =  {}  이건 셋트도되고 딕셔너리도되서 안되겟다
    while True:
        num = math.ceil(random.random() * 45) #랜덤 모듈에서 랜덤메서드를 불러와서 값을 생성하면 0~1 사이 수 생성해서 45를 곱하고 다시 무조건 올리햄버림
        lotto_set.add(num)
        if len(lotto_set) == 6: # 셋의 총 갯수를 구함 무한반복중 원소를 추가하다가 갯수가 6이되면 스탑
            #  len내장함수로 갯수구하기
            break
    return list(lotto_set) # 내장클래스인 list로 셋자료구조를 리스트화함
if __name__ == "__main__":
    for i in range(5):
        lotto_nums = lotto() # 리스트로 만들어서 참조한다
        lotto_nums.sort() # 리스트 객체의 sort메서드 수행
        print(lotto_nums)