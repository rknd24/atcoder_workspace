n = int(input())
s = input()
dp = [0]*8
dp[0] = 1
goal = "atcoder"
for i in s:
    for j in range(7,0,-1):
        if goal[j-1] == i:
            dp[j] += dp[j-1]
dp[7] %= (10**9+7)
print(dp[7])



    
