a = input()
n = 0
for i in range(len(a)):
    if 65 <= ord(a[i]) <= 67:
        n += 3
    elif 68 <= ord(a[i]) <= 70:
        n += 4
    elif 71 <= ord(a[i]) <= 73:
        n += 5
    elif 74 <= ord(a[i]) <= 76:
        n += 6
    elif 77 <= ord(a[i]) <= 79:
        n += 7
    elif 80 <= ord(a[i]) <= 83:
        n += 8
    elif 84 <= ord(a[i]) <= 86:
        n += 9
    elif 87 <= ord(a[i]) <= 90:
        n += 10
print(n)
