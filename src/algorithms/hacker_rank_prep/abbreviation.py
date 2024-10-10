def abbreviation(a, b):
    # Write your code here
    dp=[ [1]+ [0]*(len(b)) for i in range(len(a)+1)]
    # dp[i][0] always 1('YES') cuz b got 0 length
    
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                # same upper case
                dp[i][j]=dp[i-1][j-1]
            elif a[i-1]==b[j-1].lower():
                # same lower case
                dp[i][j]=max(dp[i-1][j-1], dp[i-1][j])
            elif a[i-1].isupper():
                dp[i][j]=0
            else:
                dp[i][j]=dp[i-1][j]

    if dp[len(a)][len(b)]:
        return 'YES'
    else:
        return 'NO'
    
    
