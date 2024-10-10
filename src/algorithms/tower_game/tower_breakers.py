def divisors(m):
    c = 0
    while m % 2 == 0:
        c += 1
        m = m // 2

    for i in range(3, int(m**0.5) + 1, 2):
        while m % i == 0:
            c += 1
            m = m // i
    if m > 2:
        c += 1
    return c

def towers(n):
    global memo
    nim_sum = 0
    for i in sorted(n):
        print(i)
        if i == 1:
            continue
        else:
            if i not in memo:
                memo[i] = divisors(i)
                print(f'memo {memo[i]}')
            nim_sum ^= memo[i]
    return nim_sum

# n = 2,  m = 6 -> 2
# n = 2, m = 2 -> 2
# n = 1, m = 4 -> 1
demo = '3'
memo = {}
for _ in range(2):
    print(2 if towers([int(x) for x in demo.split()]) == 0 else 1)