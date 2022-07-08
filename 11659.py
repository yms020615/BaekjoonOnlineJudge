import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0]

sum = 0
for i in a:
    sum += i
    s.append(sum)

for _ in range(m):
    st, en = map(int, input().split())
    print(s[en] - s[st-1])
