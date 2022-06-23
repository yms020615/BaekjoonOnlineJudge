#include <iostream>
#include <string>
#include <algorithm>
#define FAST cin.tie(NULL); cout.tie(NULL); ios::sync_with_stdio(false)
using namespace std;

int n, t;
int suffix[100001], lcp[100001], temp[100001], g[100001], tg[100001];
string s;

bool compare(int a, int b) {
    if (g[a] == g[b])
        return g[a+t] < g[b+t];
    return g[a] < g[b];
}

void SuffixArray(string str) {
    t = 1;
    n = str.length();
    for (int i = 0; i < n; i++) {
        suffix[i] = i;
        g[i] = str[i];
    }

    while (t <= n) {
        g[n] = -1;
        sort(suffix, suffix + n, compare);
        tg[suffix[0]] = 0;

        for (int i = 1; i < n; i++)
            if (compare(suffix[i-1], suffix[i]))
                tg[suffix[i]] = tg[suffix[i-1]] + 1;
            else
                tg[suffix[i]] = tg[suffix[i-1]];

        for (int i = 0; i < n; i++)
            g[i] = tg[i];
        t *= 2;
    }
}

void LCP() {
    for (int i = 0; i < n; i++)
        temp[suffix[i]] = i;

    int len = 0;
    for (int i = 0; i < n; i++) {
        if (temp[i]) {
            int j = suffix[temp[i] - 1];
            while (s[j + len] == s[i + len])
                len++;
            lcp[temp[i]] = len;
            if (len)    
                len--;
        }
    }
}

int main() {
    FAST;
    int tc;
    cin >> tc;
    while (tc--) {
        cin >> s;
        SuffixArray(s);
        LCP();
        int ans = 0;
        for (int i = 1; i < n; i++)
            if (lcp[i-1] < lcp[i])
                ans += lcp[i] - lcp[i-1];
        cout << ans << '\n';
    }
}
