input = __import__('sys').stdin.readline

n, b, c = map(int, input().split())
a = list(map(int, input().split())) + [0, 0]

if b < c:
    c = b
ans = 0

for i in range(n):
    if a[i + 1] > a[i + 2]:
        temp = min(a[i], a[i + 1] - a[i + 2])
        ans += (b + c) * temp
        a[i] -= temp
        a[i + 1] -= temp

        temp = min(a[i], a[i + 1], a[i + 2])
        ans += (b + 2 * c) * temp
        a[i] -= temp
        a[i + 1] -= temp
        a[i + 2] -= temp

    else:
        temp = min(a[i], a[i + 1], a[i + 2])
        ans += (b + 2 * c) * temp
        a[i] -= temp
        a[i + 1] -= temp
        a[i + 2] -= temp

        temp = min(a[i], a[i + 1])
        ans += (b + c) * temp
        a[i] -= temp
        a[i + 1] -= temp

    ans += b * a[i]

print(ans)
