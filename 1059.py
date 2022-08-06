input = __import__('sys').stdin.readline

l = int(input())
s = list(map(int, input().split()))
n = int(input())

if n in s:
    print(0)
    exit(0)

s.sort(reverse = True)
temp = 0
while s[-1] < n:
    temp = s.pop()
s.append(temp)

print((s[-2] - n) * (n - s[-1]) - 1)
