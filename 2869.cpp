#include <bits/stdc++.h>

using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	double a, b, v;
	cin >> a >> b >> v;

	double ans = (v - b) / (a - b);
	cout << int(ceil(ans));
}
