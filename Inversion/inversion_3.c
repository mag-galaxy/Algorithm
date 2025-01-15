#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>

long long int merge_aux(int *a, int *temp, int p, int r);
long long int merge_inver(int *a, int *temp, int p, int q, int r);

void Print_array(int *a, int n){
    for(int i = 0; i < n; ++i){
        printf("%d,", a[i]);
    }
}

long long int count_inversion(int *a, int a_size){
    int * temp = (int*)malloc(sizeof(int) * a_size);
    return merge_aux(a, temp, 0, a_size-1);
}

long long int merge_inver(int *a, int *temp, int p, int q, int r){
    int i = p;// p to q-1
    int j = q;// q to r
    int k = p;
    long long int inversion = 0;

    while(i <= q-1 && j <= r){
        if(a[i] <= a[j]){// the left one is smaller
            temp[k++] = a[i++];
        }
        else{// the right one is smaller
            temp[k++] = a[j++];
            inversion = inversion + (q - i);// this one must go across the whole left subarray
        }
    }

    while(i <= q-1)// copy the left elements from left subarray to temp
        temp[k++] = a[i++];
    
    while (j <= r)// copy the left elements from right subarray to temp
        temp[k++] = a[j++];
    
    for(i = p; i <= r; i++)// copy the data from temp back to a, then a is sorted
        a[i] = temp[i];

    return inversion;
}

long long int merge_aux(int *a, int *temp, int p, int r){
    // array a, index from p to r
    long long int inver = 0;
    int q;
    if(p < r){
        q = (p+r)/2;// middle index, separate array into two parts, left and right
        inver += merge_aux(a, temp, p, q);// index from p to q
        inver += merge_aux(a, temp, q+1, r);// index from q+1 to r
        inver += merge_inver(a, temp, p, q+1, r);// merge means combine left and right subarray
    }
    return inver;
}

long long int count_inver(int *a, int a_size){
    long long int inversion = 0;
    for(int i = 0; i < a_size; ++i){
        for(int j = i+1; j < a_size; ++j){
            if(a[i] > a[j])
                inversion += 1;
        }
    }
    return inversion;
}

int main(){

    int n = 0;
    int A[10000];

    FILE *fptr;
    fptr = fopen("testdata.txt", "r");

    if(!fptr)
        printf("fail to open file");
    
    char content[10];
    int a = 0, i = 0;
    while(fgets(content, 10, fptr) != NULL){
        int num = atoi(content);
        if(a==0){
            n = num;
            ++a;
        }
        else{
            A[i] = num;
            ++i;
        }
    }
    fclose(fptr);

    printf("n = %d\n", n);

    clock_t start, end;
    start = clock();
    long long int ans = count_inversion(&A[0], n);
    end = clock();
    double diff1 = end-start;
    printf("nlgn: %lf\n", diff1 / CLOCKS_PER_SEC);

    start = clock();
    ans = count_inver(&A[0], n);
    end = clock();
    double diff2 = (end-start);
    printf("n^2: %lf\n", diff2 / CLOCKS_PER_SEC);

    FILE *wf;
    wf = fopen("result.txt", "a");
    fprintf(wf, "%d\n", n);
    fprintf(wf, "%lf\n", diff1 / CLOCKS_PER_SEC);
    fprintf(wf, "%lf\n", diff2 / CLOCKS_PER_SEC);
    fclose(wf);

    return 0;
}