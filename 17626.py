import sys
input = sys.stdin.readline

n = int(input())
p = 4

if int(int(n ** 0.5) ** 2) == n:
    p = 1

if p == 4:
    for i in range(1, int(n ** 0.5) + 1):
        for j in range(i, int(n ** 0.5) + 1):
            if i*i + j*j == n:
                p = 2
                break

if p == 4:
    for i in range(1, int(n ** 0.5) + 1):
        for j in range(i, int(n ** 0.5) + 1):
            for k in range(j, int(n ** 0.5) + 1):
                if i*i + j*j + k*k == n:
                    p = 3
                    break

print(p)
