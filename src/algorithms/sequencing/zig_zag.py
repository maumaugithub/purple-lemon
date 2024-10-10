def findZigZagSequence(a, n):
    a.sort()
    print(f'sorted: {a}')
    mid = int((n + 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]
    print(f'first left swap {a} {mid}') 
    # original code:
    # st = mid + 1
    # ed = n - 1
    st = mid - 1
    ed = mid
    print(f'first left swap {a} {mid} {st} {ed}') 
    while(0 <= st <= ed <= n-1):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1
        print(f'{a} {mid} {st} {ed}')

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return a

# test_cases = '1 2 3 4 5 6 7'
test_cases = '2 3 5 1 4'
# expected = [1, 4, 5, 3, 2]
# expected = '1 2 3 7 6 5 4'
# for cs in range (7):
# n = 7
n = 5
a = list(map(int, test_cases.split()))
result = findZigZagSequence(a, n)
print(f'final result {result}')
    # assert(result.__eq__(expected))



