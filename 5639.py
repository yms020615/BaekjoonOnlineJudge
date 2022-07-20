import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break

post = []
def postorder(root, pre):
    left, right = [], []
    root1, root2 = 0, 0

    for i in pre:
        if i < root:
            if not left:
                root1 = i
            left.append(i)

        elif i > root:
            if not right:
                root2 = i
            right.append(i)

    if root1:
        postorder(root1, left)
    if root2:
        postorder(root2, right)

    post.append(root)

postorder(pre[0], pre)
for i in post:
    print(i)
