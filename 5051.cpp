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

vector<double> multiply(vector<double> &a, vector<double> &b) {
    int n = 1;
    while (n < a.size() + b.size())
        n *= 2;

    a.resize(n);
    vector<cpx> x(n);
    for (int i = 0; i < n; i++)
        x[i] = cpx(a[i], 0);
    FFT(x, false);

    b.resize(n);
    vector<cpx> y(n);
    for (int i = 0; i < n; i++)
        y[i] = cpx(b[i], 0);
    FFT(y, false);

    vector<cpx> c(n);
    for (int i = 0; i < n; i++)
        c[i] = x[i] * y[i];
    FFT(c, true);

    vector<double> z(n);
    for (int i = 0; i < n; i++)
        z[i] = (double)round(c[i].real());

    return z;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;

	vector<int> a(n), b(n);
	for (int i = 1; i < n; i++) {
		a[(1LL * i * i) % n]++;
		b[(2LL * i * i) % n]++;
	}

	vector<double> p(n);
	for (int i = 0; i < n; i++)
		p[i] = a[i];

	vector<double> c = multiply(p, p);
	long long ans = 0;
	for (int i = 1; i < n; i++) {
		int k = (1LL * i * i) % n;
		int total = c[k] + c[n + k];
		int equal = b[k];
		ans += (total - equal) / 2 + equal;
	}

	cout << ans << '\n';
}
