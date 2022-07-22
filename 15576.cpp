#include <bits/stdc++.h>

using namespace std;

const double PI = acos(-1);
typedef complex<double> cpx;

void FFT(vector<cpx> &f, bool inv) {
    int n = f.size();

    for (int i = 1, j = 0; i < n; i++) {
        int bit = n / 2;

        while (j >= bit) {
            j -= bit;
            bit /= 2;
        }
        j += bit;

        if (i < j)
            swap(f[i], f[j]);
    }

    for (int k = 1; k < n; k *= 2) {
        double angle = inv ? PI / k : -PI / k;
        cpx dir(cos(angle), sin(angle));

        for (int i = 0; i < n; i += k * 2) {
            cpx unit(1, 0);

            for (int j = 0; j < k; j++) {
                cpx u = f[i + j];
                cpx v = f[i + j + k] * unit;

                f[i + j] = u + v;
                f[i + j + k] = u - v;

                unit *= dir;
            }
        }
    }

    if (inv)
        for (int i = 0; i < n; i++)
            f[i] /= n;
}

vector<cpx> multiply(vector<cpx> &a, vector<cpx> &b) {
    int n = 1;
    while (n < a.size() + b.size())
        n *= 2;

    a.resize(n);
    FFT(a, false);

    b.resize(n);
    FFT(b, false);

    vector<cpx> c(n);
    for (int i = 0; i < n; i++)
        c[i] = a[i] * b[i];
    FFT(c, true);

    return c;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    string A, B;
    cin >> A >> B;

    vector<cpx> a, b;
    for (int i = A.size() - 1; i >= 0; i--)
        a.push_back(A[i] - '0');
    for (int i = B.size() - 1; i >= 0; i--)
        b.push_back(B[i] - '0');

    int size = a.size() + b.size() - 1;
    vector<cpx> c = multiply(a, b);
    vector<int> ans(size);

    for (int i = 0; i < size; i++) {
        ans[i] = (int)(c[i].real() + 0.5);
    }

    for (int i = 0; i < size - 1; i++) {
        ans[i + 1] += ans[i] / 10;
        ans[i] %= 10;
    }

    while (!ans.empty() && ans.back() == 0)
        ans.pop_back();

    if (ans.empty())
        ans.push_back(0);
    reverse(ans.begin(), ans.end());

    for (int i : ans)
        cout << i;
}
