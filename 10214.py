input = __import__('sys').stdin.readline

for _ in range(int(input())):
    y, k = 0, 0

    for i in range(9):
        a, b = map(int, input().split())
        y += a
        k += b

    if y < k:
        print('Korea')
    elif y == k:
        print('Draw')
    else:
        print('Yonsei')
