def lcs_brute(str1, str2, m, n):
    if(m == -1 or n == -1):
        return 0
    if(str1[m] == str2[n]):
        return 1 + lcs_brute(str1, str2, m-1, n-1)
    return max(lcs_brute(str1, str2, m-1, n), lcs_brute(str1, str2, m, n-1))