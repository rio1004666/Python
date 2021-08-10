import random
#help(random)

r = random.random() # 랜덤 라이브러리의 랜덤 메서드는 0~1 사이의 랜덤수를 뽑아냄
print(r)

cnt = 0
lst = []
while True:
    r = random.random()
    #print(random.random())
    if r < 0.3:
        break
    else:
        r *= 2
        lst.append(r)
        cnt += 1
print(lst)
