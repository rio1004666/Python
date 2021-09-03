
n = int(input('정렬할 데이터의 갯수를 입력하세요(1~500개제한)'))
array = []
for i in range(n):
    num = int(input('1이상 100,000이하의 수를 입력하세요=>'))
    array.append(num)


array.sort(reverse=True)
for num in array:
    print(num,end=" ")