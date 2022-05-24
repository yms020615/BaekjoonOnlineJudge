input = __import__('sys').stdin.readline

n, k = map(int, input().split())
fact = [1, 1]
for i in range(2, 401):
    fact.append(i * fact[i-1])
print((fact[n+k-1]//(fact[k-1]*fact[n])) % 1000000000)
