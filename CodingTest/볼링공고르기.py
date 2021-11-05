from itertools import combinations

N,M = map(int, input().split())
boling_balls = list(map(int,input().split()))

com = list(combinations(boling_balls,2))
final_com = []
for a,b in com:
    if a == b:
        continue
    else:
        final_com.append((a,b))

print(len(final_com))