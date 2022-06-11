input = __import__('sys').stdin.readline

while True:
    t = input().rstrip()
    if t == '.':
        break
    if len(set(t)) == 1:
        print(len(t))
        continue

    find = 0
    for i in range(1, len(t) // 2 + 1):
        if len(t) % i:
            continue

        m = len(t) // i
        p = t[:i] * m
        table = [0] * len(p)
        if t == p:
            find = max(find, m)
    print(find if find else 1)
