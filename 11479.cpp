#include <iostream>
#include <string>
#include <algorithm>
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
    cin >> s;
    SuffixArray(s);
    LCP();
    long long int ans = 0;
    for (int i = 0; i < n; i++)
        ans += suffix[i] + 1;
    for (int i = 1; i < n; i++)
        ans -= lcp[i];
    cout << ans;
}
