x = int(input())

a = [[0 for j in range(2)] for i in range(x)]

for i in range(x):
    a[i] = list(map(int, input().split()))

a= sorted(a)

for i in range(x):
    print(a[i][0], a[i][1])
