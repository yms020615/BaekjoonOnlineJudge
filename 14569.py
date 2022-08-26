input = __import__('sys').stdin.readline

n = int(input())
time = [0 for _ in range(n)]

for i in range(n):
    s = list(map(int, input().split()))

    for j in s[1:]:
        time[i] |= 1 << j

m = int(input())
student = [0 for _ in range(m)]

for i in range(m):
    s = list(map(int, input().split()))

    for j in s[1:]:
        student[i] |= 1 << j

for i in student:
    count = 0

    for j in time:
        if i & j == j:
            count += 1

    print(count)
