#include <bits/stdc++.h>
#define _USE_MATH_DEFINES
#include <math.h>
using namespace std;

int dp[30] = {1, 5, 11, 36};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int tc, n, temp = 5;
    cin >> tc;

    while (tc--) {
        cin >> n;
        if (dp[n-1] == 0)
            for (int i = temp - 1; i < n; i++)
                dp[i] = dp[i-1] + dp[i-2] * 5 + dp[i-3] - dp[i-4];
        cout << dp[n-1] << endl;
        temp = max(temp, n);
    }
}
