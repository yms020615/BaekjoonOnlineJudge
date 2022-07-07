input = __import__('sys').stdin.readline

a = []

def solve(num):
    mod = num % 10
    num *= 10

    if num > 9999999999:
        return

    for i in range(mod):
        a.append(num + i)
        solve(num + i)

n = int(input())
for i in range(10):
    a.append(i)
    solve(i)

a.sort()
print(a[n] if n < len(a) else -1)
