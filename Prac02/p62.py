

cnt = tot = 0

while cnt < 5:

    cnt += 1
    tot += cnt
    print(cnt, tot)

dataset = [] # 리스트 자료구조

while cnt < 100:

    cnt += 1
    if cnt % 3 ==0:
        tot += cnt
        dataset.append(cnt) # 리스트 자료구조는 삽입 삭제가 가능하다

print('1~100 사이 3의 배수합 : %d' % tot)
print('dataset: ', dataset)
dataset.remove(99) # 99 원소를 제거 특정원소
dataset.pop() # 마지막 원소를 제거
print('dataset에서 99를 뺐다: ', dataset)
