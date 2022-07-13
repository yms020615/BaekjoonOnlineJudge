#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

class matrix {
public:
    vector<vector<int>> m;
    matrix(int n = 0): m(n, vector<int>(n)) {}
    vector<int>& operator [] (int i) { return m[i]; }
    matrix& operator += (matrix m) {return *this = *this + m; }
    matrix& operator *= (matrix m) {return *this = *this * m; }

    friend matrix operator + (matrix a, matrix b) {
        int n = a.m.size();
        matrix ret(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                ret[i][j] = (a[i][j] + b[i][j]) % 1000;
            }
        }
        return ret;
    }

    friend matrix operator * (matrix a, matrix b) {
        int n = a.m.size();
        matrix ret(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    ret[i][j] += a[i][k] * b[k][j];
                    ret[i][j] %= 1000;
                }
            }
        }
        return ret;
    }
}I;

matrix power(matrix m, int n) {
    matrix ret = I;
    for (; n; n >>= 1) {
        if (n & 1) ret *= m;
        m *= m;
    }
    return ret;
}

int main() {
    int t;
    I = matrix(2);
    I[0][0] = I[1][1] = 1;
    I[0][1] = I[1][0] = 0;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        int n;
        scanf("%d", &n);

        matrix a = matrix(2);
        a[0][0] = 6; a[0][1] = -4, a[1][0] = 1, a[1][1] = 0;
        matrix res = power(a, n-1);
        string ans = to_string((((28 * res[1][0] + 6 * res[1][1]) - 1) % 1000 + 1000) % 1000);
        while (ans.length() < 3) {
            ans = "0" + ans;
        }

        cout << "Case #" << i << ": " << ans << "\n";
    }
}
