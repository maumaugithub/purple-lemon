def luckBalance(k, contests):
    important = []
    optional = 0
    for luck, importance in contests:
        if importance:
            important.append(luck)
        else:
            optional += luck
            
    if k < len(important):
        s = sorted(important)
        i = len(s) - k
        return optional + sum(s[i:]) - sum(s[:i])
        
    return optional + sum(important)
    
    
    
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     contests = []

#     for _ in range(n):
#         contests.append(list(map(int, input().rstrip().split())))

#     result = luckBalance(k, contests)

#     fptr.write(str(result) + '\n')

#     fptr.close()

n = 5
contests = []