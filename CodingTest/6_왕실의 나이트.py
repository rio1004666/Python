from string import ascii_lowercase
a=ascii_lowercase
print(a)
input_data = input()
row = int(input_data[1]) # 1
# 아스키코드로 표현 ord
column = int(ord(input_data[0])) - int(ord('a')) + 1   # 1

cnt = 0
dx = [2,2,-2,-2,-1,1,-1,1]
dy = [1,-1,1,-1,2,2,-2,-2]
cnt = 0
for num in range(8):
    temp_row = row
    temp_column = column
    temp_row += dx[num]
    temp_column += dy[num]
    if ((1<= temp_row <=8) and (1<= temp_column <= 8)):
       cnt += 1
print(cnt)
