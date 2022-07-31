import sys
input = sys.stdin.readline

prime = [False] + [False] + [True] * 999999
for i in range(2, 1001):
    if prime[i] == True:
       for j in range(2*i, 1000001, i):
           prime[j] = False

for _ in range(int(input())):
    a = int(input())
    count = 0
    for i in range(2, a//2 + 1):
        if prime[i] and prime[a - i]:
            count += 1
    print(count)
