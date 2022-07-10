import sys
input = sys.stdin.readline

n = int(input())
i = [0 for i in range(1001)]
i[1] = 1
i[2] = 3
for j in range(3, n+1):
    i[j] = (i[j-1] + 2 * i[j-2]) % 10007
print(i[n])
