import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

dp = [s[0]]

for i in range(n-1):
    dp.append(max(s[i+1], dp[i] + s[i+1]))

print(max(dp))
