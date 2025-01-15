#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lcs_len(char x[], char y[], int m, int n){
    int c[n+1][n+1];    //n * n
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

int main(){
    char a[] = "ABCD";
    char b[] = "ABC";
    int len_a = strlen(a);
    int len_b = strlen(b);
    printf("len of a: %d\n", len_a);
    printf("len of b: %d\n", len_b);

    int answer = lcs_len(a, b, len_a, len_b);
    printf("%d", answer);

    return 0;
}