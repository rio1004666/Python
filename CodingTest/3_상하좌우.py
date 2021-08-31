n = int(input())
x, y = 1, 1
dy = [0,0,-1,1] # R L U D
dx = [1,-1,0,0]
idx = 0
plans = input().split()
while n >= 0:
    if plans[idx] == 'R':
        y += dy[0]
        x += dx[0]
        if y <= 0 or x <= 0:
            y -= dy[0]
            x -= dx[0]
    if plans[idx] == 'L':
        y += dy[1]
        x += dx[1]
        if y <= 0 or x <= 0:
            y -= dy[1]
            x -= dx[1]
    if plans[idx] == 'U':
        y += dy[2]
        x += dx[2]
        if y <= 0 or x <= 0:
            y -= dy[2]
            x -= dx[2]
    if plans[idx] == 'D':
        y += dy[3]
        x += dx[3]
        if y <= 0 or x <= 0:
            y -= dy[3]
            x -= dx[3]
    idx += 1
    n -= 1
print('y: %d,x: %d' % (y, x))

for plan in plans:
    if plan == 'L':
        if y == 1: # 그냥 y가 1일때 점프한다 계산안하고
            continue
        else:
            y -= 1
    elif plan == 'R':
        y += 1
        if y == n:
            continue
        else:
            y += 1
    elif plan == 'U':
        x -= 1
        if y <= 0:
            y +=1
    elif plan == 'D':
        x += 1
        if y <= 0:
            y +=1
print(x,y)
