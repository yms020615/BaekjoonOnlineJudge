import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = []
if m:
    s = list(map(int, input().split()))

ans = abs(100 - n)
for i in range(1000001):
    i = str(i)
    len_i = len(i)
    for j in range(len_i):
        if int(i[j]) in s:
            break
        elif j == len_i - 1:
            ans = min(ans, abs(int(i) - n) + len_i)
    
print(ans)
