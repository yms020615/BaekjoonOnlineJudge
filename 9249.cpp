#include <iostream>
#include <string>
#include <algorithm>
#define FAST cin.tie(NULL); cout.tie(NULL); ios::sync_with_stdio(false)
using namespace std;

int n, t;
int suffix[1000001], lcp[1000001], temp[1000001], g[1000001], tg[1000001];
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
        g[i] = str[i] - 'a';
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
    string s1, s2;
    cin >> s1;
    cin >> s2;
    s = s1 + '$' + s2;
    SuffixArray(s);
    LCP();
    int ans = 0, idx = 0;
    int len_s1 = s1.length();
    for (int i = 1; i < n; i++)
        if (suffix[i-1] < len_s1 && len_s1 < suffix[i] || suffix[i] < len_s1 && len_s1 < suffix[i-1])
            if (lcp[i] <= len_s1)
                if (ans < lcp[i]) {
                    ans = lcp[i];
                    idx = suffix[i];
                }
    cout << ans << endl;
    cout << s.substr(idx, ans);
}
