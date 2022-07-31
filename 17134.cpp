#include <bits/stdc++.h>

using namespace std;

const double PI = acos(-1);
typedef complex<double> cpx;
bool sieve[1000001];

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

vector<int> multiply(vector<int> &a, vector<int> &b) {
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

    vector<int> z(n);
    for (int i = 0; i < n; i++)
        z[i] = (int)round(c[i].real());

    return z;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

	memset(sieve, true, sizeof(sieve));
	sieve[0] = sieve[1] = false;
	for (int i = 2; i * i <= 1000000; i++)
		if (sieve[i])
			for (int j = 2 * i; j <= 1000000; j += i)
				sieve[j] = false;

    vector<int> a(1000001), b(1000001);
	for (int i = 2; i <= 1000000; i++)
		if (sieve[i] == true) {
			if (i * 2 <= 1000000)
				b[i * 2] = 1;
			if (i % 2)
				a[i] = 1;
		}

	vector<int> c = multiply(a, b);

	int t;
	for (cin >> t; t--;) {
		int n;
		cin >> n;
		cout << c[n] << '\n';
	}
}
