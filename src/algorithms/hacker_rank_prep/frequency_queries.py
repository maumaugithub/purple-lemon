from collections import defaultdict

def freqQuery(queries):
    memo = defaultdict()
    res = []
     
    for query in queries:
        operation, element = query
        
        if operation == 1:
            memo.setdefault(element, 0)
            memo[element] += 1
            
        elif operation == 2 and memo.get(element):
            memo[element] -= 1
            
        elif operation == 3:
            matched = element in memo.values()
            print(1 if matched else 0)
            # result.append(1) if matched else result.append(0)
            
    return res

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     queries = []

#     for _ in range(q):
#         queries.append(list(map(int, input().rstrip().split())))

#     ans = freqQuery(queries)

#     fptr.write('\n'.join(map(str, ans)))
#     fptr.write('\n')

#     fptr.close()
