input = __import__('sys').stdin.readline

n = int(input())
a = list(map(int, input().split())) + [0, 0]

ans = 0

for i in range(n):
    if a[i + 1] > a[i + 2]:
        temp = min(a[i], a[i + 1] - a[i + 2])
        ans += 5 * temp
        a[i] -= temp
        a[i + 1] -= temp

        temp = min(a[i], a[i + 1], a[i + 2])
        ans += 7 * temp
        a[i] -= temp
        a[i + 1] -= temp
        a[i + 2] -= temp

    else:
        temp = min(a[i], a[i + 1], a[i + 2])
        ans += 7 * temp
        a[i] -= temp
        a[i + 1] -= temp
        a[i + 2] -= temp

        temp = min(a[i], a[i + 1])
        ans += 5 * temp
        a[i] -= temp
        a[i + 1] -= temp

    ans += 3 * a[i]

print(ans)
