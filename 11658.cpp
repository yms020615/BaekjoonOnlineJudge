#include <bits/stdc++.h>
#define FAST cin.tie(NULL); cout.tie(NULL); ios::sync_with_stdio(false)
using namespace std;

int mat[1111][1111];
int n, m;

int sum(int x, int y) {
    int ret = 0;
    for (int i = x; i > 0; i -= (i & -i))
        for (int j = y; j > 0; j -= (j & -j))
            ret += mat[i][j];
    return ret;
}

void update(int x, int y, int val) {
    for (int i = x; i <= n; i += (i & -i))
        for (int j = y; j <= n; j += (j & -j))
            mat[i][j] += val;
}

int main() {
    FAST;
    cin >> n >> m;

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++) {
            int temp;
            cin >> temp;
            update(i, j, temp);
        }

    int q[5];
    while (m--) {
        cin >> q[0];
        if (q[0] == 0) {
            cin >> q[1] >> q[2] >> q[3];
            int temp = sum(q[1], q[2]) - sum(q[1] - 1, q[2]) - sum(q[1], q[2] - 1) + sum(q[1] - 1, q[2] - 1);
            update(q[1], q[2], q[3] - temp);
        }
        else {
            cin >> q[1] >> q[2] >> q[3] >> q[4];
            cout << sum(q[3], q[4]) - sum(q[1] - 1, q[4]) - sum(q[3], q[2] - 1) + sum(q[1] - 1, q[2] - 1) << '\n';
        }
    }
}
