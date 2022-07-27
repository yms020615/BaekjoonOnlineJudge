#include <iostream>
#include <math.h>

using namespace std;
typedef long long ll;

int main() {
	bool prime[4000001] = { 1, 1 };
	ll n, k, m;
    m = 1000000007;
	cin >> n >> k;

	for (ll i = 2; i * i <= n; i++) {
		if (!prime[i]) {
			ll j = 2;
			while (i * j <= n) {
				prime[i * j] = 1;
				j += 1;
			}
		}
	}

	ll ans = 1;
	ll leg[4000001] = { 0 };

	for (ll i = 2; i <= n; i++) {
		if (!prime[i]) {
			for (ll j = 1; i * j <= n; j++) {
				ll q = pow(i, j);
				leg[i] += (n / q) - ((n - k) / q) - (k / q);
			}
		}
	}

	for (ll i = 1; i <= n; i++) {
		for (ll j = 1; j <= leg[i]; j++) {
			ans *= i;
			ans %= m;
		}
	}

	cout << ans % m;
}
