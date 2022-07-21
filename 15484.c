#include <bits/stdc++.h>

using namespace std;

int min_editdistance(string str1, string str2);
static int __GetMin3(int a, int b, int c);
static int __GetMin4(int a, int b, int c, int d);

int min_editdistance(string str1, string str2) {
	int n = str1.length();
	int m = str2.length();
	int d[n + 2][m + 2];
    int s[128];
    fill_n(s, 128, 1);

	d[0][0] = n + m;

	for (int i = 1; i <= n + 1; i++) {
		d[i][0] = n + m;
        d[i][1] = i - 1;
    }
	
	for (int i = 1; i <= m + 1; i++) {
		d[0][i] = n + m;
        d[1][i] = i - 1;
    }

	for (int i = 2; i <= n + 1; i++) {
        int temp = 1;

		for (int j = 2; j <= m + 1; j++) {
            int k = s[str2[j - 2]];
            int l = temp;
            int t_cost = (i - k - 1) + 1 + (j - l - 1);

            int s_cost;
            if (str1[i - 2] == str2[j - 2]) {
			    s_cost = 0;
                temp = j;
            }
            else
                s_cost = 1;

            d[i][j] = __GetMin4(d[i - 1][j - 1] + s_cost, d[i][j - 1] + 1, d[i - 1][j] + 1, d[k - 1][l - 1] + t_cost);
		}
        s[str1[i - 2]] = i;
	}
	
	return d[n + 1][m + 1];
}

static int __GetMin3(int a, int b, int c)
{
	int min = a;
	if (b < min)
		min = b;
	if (c < min)
		min = c;
	return min;
}

static int __GetMin4(int a, int b, int c, int d)
{
	int min = __GetMin3(a, b, c);
	return (min > d) ? d : min;
}

int main()
{
	string str1;
    string str2;

    cin >> str1;
    cin >> str2;
	
	int distance;
    distance = min_editdistance(str1, str2);
    cout << distance;
}
