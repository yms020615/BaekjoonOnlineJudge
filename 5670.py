import sys
input = sys.stdin.readline

class Node:
    def __init__(self, key, count = 0):
        self.key = key
        self.child = {}
        self.count = count
        self.check = False

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, s):
        cur_node = self.root
        for c in s:
            if c not in cur_node.child:
                cur_node.child[c] = Node(c)
            cur_node = cur_node.child[c]
        cur_node.check = True

    def search(self, s):
        i = 0
        cur_node = self.root
        for c in s:
            cur_node = cur_node.child[c]
            if len(cur_node.child) > 1 or cur_node.check:
                i += 1
        return i

while True:
    t = Trie()
    words = []

    try:
        n = int(input())
    except:
        break

    for _ in range(n):
        s = input().rstrip()
        t.insert(s)
        words.append(s)
    result = 0
    for word in words:
        result += t.search(word)

    print('%.2f' % (result / n))
