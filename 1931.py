input = __import__('sys').stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.sort(key = lambda x: (x[1], x[0]))
count = 1
end = a[0][1]

for i in a[1:]:
    if i[0] >= end:
        count += 1
        end = i[1]

print(count)
