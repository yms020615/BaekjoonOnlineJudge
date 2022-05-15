import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort(reverse = True)
b.sort(reverse = True)

if a[0] < b[0]:
    print(-1)
    exit(0)

ans = 0
while b:
    ans += 1
    for i in a:
        for j in b:
            if i >= j:
                b.remove(j)
                break

print(ans)
