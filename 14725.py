import sys
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, s):
        cur_node = self.root
        for c in s:
            if c not in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]
        cur_node[0] = True

    def search(self, s, level):
        if 0 in s:
            return

        s_child = sorted(s)

        for c in s_child:
            print('--' * level + c)
            self.search(s[c], level + 1)

n = int(input())
tr = Trie()
for _ in range(n):
    p = list(input().strip().split())
    k, t = int(p[0]), p[1:]
    tr.insert(t)
tr.search(tr.root, 0)
