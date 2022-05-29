#include <stdio.h>
#include <iostream>
#include <stdlib.h>
using namespace std;

int inorder[100000];
int postorder[100000];
int pos[100001];

void preorder(int ins, int ine, int posts, int poste)
{
	if (ins > ine || posts > poste)
		return;

	cout << postorder[poste] << ' ';
	int r = pos[postorder[poste]];

	preorder(ins, r - 1, posts, posts + r - ins - 1);
	preorder(r + 1, ine, posts + r - ins, poste - 1);
}

int main()
{
	int n;
	cin >> n;

	for (int i = 0; i < n; i++)
		cin >> inorder[i];
	for (int i = 0; i < n; i++)
		cin >> postorder[i];
	for (int i = 0; i < n; i++)
		pos[inorder[i]] = i;

	preorder(0, n - 1, 0, n - 1);
}
