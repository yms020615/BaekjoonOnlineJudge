a = int(input())
n = 0
while n*(n-1)/2 < a:
    n+=1
b = n*(n-1)/2
c = b-a
if n%2==0:
    print('{}/{}'.format(int(c+1), int(n-c-1)))
else:
    print('{}/{}'.format(int(n-c-1), int(c+1)))
