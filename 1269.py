n, m = map(int, input().split())
print(len(set(map(int, input().split())) ^ set(map(int, input().split()))))
