import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = list(map(int, input().split()))
    sum = 0
    for i in range(1, len(a)):
        for j in range(1, len(a)):
            n = 0
            if i < j:
                for k in range(min(a[i], a[j]), 0, -1):
                    if a[i] % k == 0 and a[j] % k == 0:
                        n = k
                        break
            sum += n
    print(sum)
