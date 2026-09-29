n = int(input())
s = input()
dp = [0]*8
dp[0] = 1
target = "atcoder"
for i in range(n):
    for j in range(7,0,-1):
        if s[i] == target[j-1]:
            dp[j] += dp[j-1]
            dp[j] %= (10**9 + 7)
print(dp[7])

