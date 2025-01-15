#include <iostream>
using namespace std;

int lcs_len(string x, string y, int m, int n){
    int c[m+1][n+1];    //c[0:m][0:n]
    for(int i = 0; i <= m; ++i)
        c[i][0] = 0;
    for(int j = 0; j <= n; ++j)
        c[0][j] = 0;
    
    for(int i = 1; i <= m; ++i){
        for(int j = 1; j <= n; ++j){
            if(x[i-1] == y[j-1])
                c[i][j] = c[i-1][j-1]+1;
            else if(c[i-1][j] >= c[i][j-1])
                c[i][j] = c[i-1][j];
            else
                c[i][j] = c[i][j-1];
        }
    }
    return c[m][n];
}

int mian(){
    string a = "";
    string b = "";
    cin >> a >> b;
    cout << lcs_len(a, b, a.length(), b.length());
    return 0;
}