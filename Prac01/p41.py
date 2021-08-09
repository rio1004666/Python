

i = tot = 10
i += 1
tot += i
print(i)
print(tot)
print('출력1', end='') # 출력문 옵션
print('출력2')
v1, v2 = 1, 20
print(v1, v2)
#패킹 할당
lst = [1, 2, 3, 4, 5]
var1, *var2 = lst
print(var1, var2)
*var3, var4, var5, var6, var7, var8 = lst
print(var3, var4, var5, var6, var7, var8)
print(var7, var8)
var7, var8 = var8, var7
print(var7, var8)
