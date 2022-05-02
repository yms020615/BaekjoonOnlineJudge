count = 0

for i in range(int(input()) + 1):
    if 1 <= i < 100:
        count += 1

    elif 100 <= i < 1000:
        if (((i//10)%10) - i%10) == ((i//100) - ((i//10)%10)):
            count += 1

print(count)
