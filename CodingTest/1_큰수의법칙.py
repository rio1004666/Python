

n, m, k = map(int, input().split())
list1 = list(map(int, input().split()))

new_list = sorted(list1)
length = len(new_list)
first = new_list[length-1]
second = new_list[length-2]
print('가장 큰수는: ', first)
print('두번째로 큰수는: ', second)
temp = k
total = 0
for i in range(m):
    if temp == 0:
        temp = k
        total += second
    else:
        total += first
        temp -= 1




print(total)



# list1.sort(reverse=True)