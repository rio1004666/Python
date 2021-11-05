"""

날짜: 2021/10/15
이름: 강병화
내용: 코딩테스트 - 다이나믹 프로그래밍 피보나치 탑다운 처리

다이나믹 프로그래밍 탑다운(Bottom-Up)

- 재귀함수와 메모이제이션을 이용한 프로그래밍 방식

- 작은 문제부터 차근차근 해결해 나가는 방식

"""

import time

# 프로그램 실행 시간 시작

start_time = time.time()

# DP(Dynamic Programming) 테이블 생성

dp = [0] * 100
dp[0] = 0
dp[1] = 1
print(dp[0])
print(dp[1])

for n in range(2, 100):
    dp[n] = dp[n - 1] + dp[n - 2]
    print(dp[n])

#
# for i in range(1,40):
#     print(fibo(i))

# 프로그램 실행 시간 종료

end_time = time.time()

# 전체 수행시간

total_time = end_time - start_time
print('프로그램 수행시간: ', total_time)
print(dp)
