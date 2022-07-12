import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

def traversal(inL, inR, posL, posR):
    if inL > inR or posL > posR:
        return

    rootID = inorder.index(postorder[posR])
    print(postorder[posR], end = ' ')

    traversal(inL, rootID - 1, posL, posL + rootID - inL - 1)
    traversal(rootID + 1, inR, posL + rootID - inL, posR - 1)

traversal(0, n - 1, 0, n - 1)
