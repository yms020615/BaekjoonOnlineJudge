import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
rseq = seq[::-1]
dp1 = [0] * (n+1)
dp2 = [0] * (n+1)

for i in range(n):
    inc = 0
    dec = 0
    for j in range(i):
        if seq[i] > seq[j]:
            inc = max(inc, dp1[j])
        if rseq[i] > rseq[j]:
            dec = max(dec, dp2[j])
    dp1[i] = inc + 1
    dp2[i] = dec + 1

ans = []
for i in range(len(dp1)):
    ans.append(dp1[i] + dp2[len(dp2)-2-i])
print(max(ans) - 1)
