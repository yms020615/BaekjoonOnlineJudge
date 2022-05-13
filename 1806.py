import sys
input = sys.stdin.readline

n, s = map(int, input().split())
l = list(map(int, input().split()))

p1, p2, cur = 0, 0, l[0]
ans = 100001
while True:
    if cur >= s:
        ans = min(ans, p2-p1+1)
        cur -= l[p1]
        p1 += 1
    else:
        p2 += 1
        if p2 == n:
            break
        cur += l[p2]

print(ans) if ans < 100001 else print(0)
