input = __import__('sys').stdin.readline

a, d, k = map(int, input().split())
d /= 100
k /= 100

def exp(d):
    if d >= 1:
        return a

    temp = d * a + (1 - d) * (a + exp(d * (1 + k)))
    return temp

print(exp(d))
