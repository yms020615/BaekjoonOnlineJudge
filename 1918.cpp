#include <bits/stdc++.h>

using namespace std;

int icp(char op) {
    switch (op)
    {
    case '(':
        return 0;
        break;
    case '*':
    case '/':
        return 1;
        break;
    case '+':
    case '-':
        return 2;
        break;
    default:
        break;
    }
}

int isp(char op) {
    switch (op)
    {
    case '(':
        return 3;
        break;
    case '*':
    case '/':
        return 1;
        break;
    case '+':
    case '-':
        return 2;
        break;
    default:
        break;
    }
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	string s;
	cin >> s;

	stack<char> stc;

	for (char c : s) {
		if (c == ')') {
			for (; !stc.empty() and stc.top() != '('; stc.pop())
				cout << stc.top();
			stc.pop();
		}

		else if ('A' <= c and c <= 'Z') {
			cout << c;
		}

		else {
			for (; !stc.empty() and isp(stc.top()) <= icp(c); stc.pop())
				cout << stc.top();
			stc.push(c);
		}
	}

	while (!stc.empty()) {
		cout << stc.top();
		stc.pop();
	}
}
