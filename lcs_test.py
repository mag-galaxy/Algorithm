import time

def lcs_brute(str1, str2, m, n):
    if(m == -1 or n == -1):
        return 0
    if(str1[m] == str2[n]):
        return 1 + lcs_brute(str1, str2, m-1, n-1)
    return max(lcs_brute(str1, str2, m-1, n), lcs_brute(str1, str2, m, n-1))

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
with open('input.txt', 'r') as f_read:
    with open('output.txt', 'w') as f_write:
        for line in f_read:
            data_list = line.split()
            s1 = data_list[0]
            s2 = data_list[1]
            total_len = max(len(s1), len(s2))
            
            start1 = time.time()
            ans1 = lcs_brute(s1, s2, len(s1)-1, len(s2)-1)
            end1 = time.time()

            start2 = time.time()
            ans2 = lcs_len(s1, s2, len(s1), len(s2))
            end2 = time.time()
            f_write.write(str(total_len) + ' ' + str(end1 - start1) + ' ' + str(end2 - start2))

f_write.close()
f_read.close()
