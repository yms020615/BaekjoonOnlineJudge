#include <bits/stdc++.h>
using namespace std;

int dp[1001][1001];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n, k;
    cin >> n >> k;

    dp[0][0] = 1;
    dp[1][0] = 1;
    dp[1][1] = 1;

    for (int i = 2; i <= n; i++)
        for (int j = 0; j <= k; j++)
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % 10007;

    cout << dp[n][k];
}
