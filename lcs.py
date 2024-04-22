def lcs_len(str1, str2, m, n):
    c = [[0]*(n+1)]*(m+1)                   #c[0:m][0:n]

    for i in range(1, m+1):                 #1~m
        for j in range(1, n+1):             #1~n
            if str1[i-1] == str2[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
    return c[m][n]

# main
x = input()
y = input()
print(lcs_len(x, y, len(x), len(y)), end = '')