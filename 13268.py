input = __import__('sys').stdin.readline

n = int(input()) % 100

if n == 0 or n == 10 or n == 30 or n == 60:
    print(0)

elif 0 < n < 10 or 10 < n <= 15 or 25 <= n < 30 or 30 < n <= 35 or 55 <= n < 60 or 60 < n <= 65 or 95 <= n < 100:
    print(1)

elif 15 < n < 25 or 35 < n <= 40 or 50 <= n < 55 or 65 < n <= 70 or 90 <= n < 95:
    print(2)

elif 40 < n < 50 or 70 < n <= 75 or 85 <= n < 90:
    print(3)

elif n == 45 or 75 < n < 85:
    print(4)

elif n == 80:
    print(5)
