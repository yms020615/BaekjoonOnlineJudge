#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
	int n;
	cin >> n;

	string s;
	cin >> s;

	vector<double> a;
	double temp;
	for (int i = 0; i < n; i++) {
		cin >> temp;
		a.push_back(temp);
	}

	stack<double> stc;
	double temp1, temp2;
	for (int i = 0; i < s.length(); i++) {
		switch (s[i]) {
			case '+':
				temp1 = stc.top();
				stc.pop();
				temp2 = stc.top();
				stc.pop();
				stc.push(temp2 + temp1);
				break;

			case '-':
				temp1 = stc.top();
				stc.pop();
				temp2 = stc.top();
				stc.pop();
				stc.push(temp2 - temp1);
				break;

			case '*':
				temp1 = stc.top();
				stc.pop();
				temp2 = stc.top();
				stc.pop();
				stc.push(temp2 * temp1);
				break;

			case '/':
				temp1 = stc.top();
				stc.pop();
				temp2 = stc.top();
				stc.pop();
				stc.push(temp2 / temp1);
				break;

			default:
				stc.push(a[s[i] - 'A']);
		}
	}

	printf("%.2f", stc.top());
}
