#include <bits/stdc++.h>

using namespace std;

#define INSERT_COST	1
#define DELETE_COST	1
#define SUBSTITUTE_COST	1
#define TRANSPOSE_COST	9999

int min_editdistance(string str1, string str2);
static int __GetMin3(int a, int b, int c);
static int __GetMin4(int a, int b, int c, int d);

int min_editdistance(string str1, string str2) {
	int n = str1.length();
	int m = str2.length();
	int d[n + 1][m + 1];

	d[0][0] = 0;

	for (int i = 0; i <= n; i++)
		d[i][0] = i;
	
	for (int i = 0; i <= m; i++)
		d[0][i] = i;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			int cost = str1[i - 1] == str2[j - 1] ? 0 : SUBSTITUTE_COST;

			if ((i > 1 && j > 1) && (str1[i - 2] == str2[j - 1] && str1[i - 1] == str2[j - 2]))
				d[i][j] = __GetMin4(d[i - 1][j - 1] + cost, d[i][j - 1] + INSERT_COST, d[i - 1][j] + DELETE_COST, d[i - 2][j - 2] + TRANSPOSE_COST);

			else
				d[i][j] = __GetMin3(d[i - 1][j - 1] + cost, d[i][j - 1] + INSERT_COST, d[i - 1][j] + DELETE_COST);
		}
	}
	
	return d[n][m];
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
