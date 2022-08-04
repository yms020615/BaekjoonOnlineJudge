s = [0, 1, 2]

for i in range(3, 43):
    s.append(1 + s[i-1] + s[i-2])
    
s.append(9999999999999)

for _ in range(int(input())):
    v = int(input())
    for i in range(len(s)):
        if s[i] <= v < s[i+1]:
            print(i)
