

n,m = map(int, input().split())

minis = []

for i in range(n):

    list1 = list(map(int, input().split()))

    minis.append(min(list1))

print(max(minis))





