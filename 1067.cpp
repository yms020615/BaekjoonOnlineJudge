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

    int n;
    cin >> n;

    vector<int> x(n), y(n);
    vector<cpx> a(2 * n), b(n);

    for (int i = 0; i < n; i++) {
        cin >> x[i];
        a[i + n] = a[i] = cpx(x[i], 0);
    }
    for (int i = n - 1; i >= 0; i--) {
        cin >> y[i];
        b[i] = cpx(y[i], 0);
    }

    int ans = 0;
    vector<cpx> c = multiply(a, b);
    for (cpx temp : c)
        ans = max(ans, (int)round(temp.real()));

    cout << ans;
}
