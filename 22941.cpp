#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	ll hp1, atk1, hp2, atk2;
	cin >> hp1 >> atk1 >> hp2 >> atk2;

	ll p, s;
	cin >> p >> s;

	ll a, b;
	a = (ll)(ceil((double)hp1 / (double)atk2));

	if (((hp2 - p) % atk1) and (((hp2 - p) % atk1 + p) <= atk1))
		b = (ll)(ceil((double)hp2 / (double)atk1));
	else
		b = (ll)(ceil((double)(hp2 + s) / (double)atk1));

	cout << (a >= b ? "Victory!" : "gg");
}
