import sys
input = sys.stdin.readline

n = int(input())
graph = [[0, 0] for _ in range(26)]
for _ in range(n):
    a, b, c = map(str, input().rstrip().split())
    graph[ord(a) - ord('A')][0] = ord(b) - ord('A')
    graph[ord(a) - ord('A')][1] = ord(c) - ord('A')

def preorder(v):
    left, right = graph[v]
    
    print(chr(v + ord('A')), end = '')

    if left != ord('.') - ord('A'):
        preorder(left)

    if right != ord('.') - ord('A'):
        preorder(right)

def inorder(v):
    left, right = graph[v]
    
    if left != ord('.') - ord('A'):
        inorder(left)

    print(chr(v + ord('A')), end = '')

    if right != ord('.') - ord('A'):
        inorder(right)

def postorder(v):
    left, right = graph[v]
    
    if left != ord('.') - ord('A'):
        postorder(left)

    if right != ord('.') - ord('A'):
        postorder(right)

    print(chr(v + ord('A')), end = '')

preorder(0)
print()
inorder(0)
print()
postorder(0)
