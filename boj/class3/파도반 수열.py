import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    dp = [0] * 101
    dp[1], dp[2], dp[3] = 1, 1, 1
    for i in range(4, n + 1):
        dp[i] = dp[i - 2] + dp[i - 3]
    print(dp[n])
