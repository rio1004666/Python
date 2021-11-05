
n = int(input())
food_depot = list(map(int, input().split()))
print(food_depot)

dp = [0] * 101
dp[0] = food_depot[0]
dp[1] = max(food_depot[0], food_depot[1])
print(dp[0],dp[1])
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + food_depot[i])

print(dp[n-1])

