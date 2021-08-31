h = int(input())

count = 0

for i in range(h+1):
    for m in range(60):
        for s in range(60):
            temp = str(i) + str(m) + str(s)
            if temp.find('3') >= 0: #문자열에 3이 포함되어 있는지 체크 하는  '3' in temp: 문자열안에 3이 있다면
                # 찾으면 0이된다
                count += 1

print(count)

#문자열로 바꾼후에 3을 포함하는  => 문자열 전환!!!!
