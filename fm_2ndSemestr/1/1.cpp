#include <bits/stdc++.h>
using namespace std;
int main()
{
	string a,b;
	ifstream file("data1.txt");
	file>>a;
	b=a;
	reverse(a.begin(),a.end());
	if(a==b)
	cout<<"This number is polynomial";
	else
	cout<<"This number is not polynomial";
}