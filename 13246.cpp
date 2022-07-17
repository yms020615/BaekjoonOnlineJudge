#include <stdio.h>
#include <vector>
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
} M, I;

matrix power(matrix m, long long int n) {
    matrix ret = I;
    for (; n; n >>= 1) {
        if (n & 1) ret *= m;
        m *= m;
    }
    return ret;
}

matrix solve(matrix m, long long int n) {
    if (n == 1) return m;
    auto ret = solve(m, n >> 1) * (I + power(m, n >> 1));
    if (n & 1) ret += power(m, n);
    return ret;
}

int main() {
    int n;
    long long int m;
    scanf("%d %lld", &n, &m);
    M = I = matrix(n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &M[i][j]);
            M[i][j] %= 1000;
            if (i == j) I[i][j] = 1;
        }
    }

    M = solve(M, m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d%c", M[i][j], j < n-1 ? ' ' : '\n');
        }
    }
}
