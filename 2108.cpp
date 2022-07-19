#include <bits/stdc++.h>
using namespace std;

int n;
int a[8001];
vector<int> b;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;

    int temp;
    for (int i = 0; i < n; i++) {
        cin >> temp;
        a[temp + 4000]++;
        b.push_back(temp);
    }

    int sum = 0;
    for (int i = 0; i <= 8000; i++) {
        sum += a[i] * (i - 4000);
    }

    double mean = double(sum) / n;
    cout << int(round(mean)) << '\n';

    sort(b.begin(), b.end());
    cout << b[n / 2] << '\n';

    int freq = 0;
    for (int i = 0; i <= 8000; i++)
        if (freq < a[i])
            freq = a[i];

    vector<int> mode;
    for (int i = 0; i <= 8000; i++)
        if (freq == a[i])
            mode.push_back(i - 4000);

    sort(mode.begin(), mode.end());

    if (mode.size() > 1)
        cout << mode[1] << '\n';
    else
        cout << mode[0] << '\n';

    cout << b[b.size() - 1] - b[0];
}
