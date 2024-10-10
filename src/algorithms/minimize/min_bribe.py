def minimumBribes(q):
    steps = calculate_steps_to_sort(q)
    print(f'steps {steps}')
    return 'Too chaotic' if steps >= len(q)-1 else steps

def calculate_steps_to_sort(q):
    i = 0
    s = sorted(q)
    s.reverse()
    q.reverse()
    size = len(q)-1
    for i in range(size):
        s[i], s[i+1] = s[i+1], s[i] 
        print(f'{s} {q}')
        if s == q:
            return i
        i += 1
    return i

# if __name__ == '__main__':
#     t = int(input().strip())

#     for t_itr in range(t):
#         n = int(input().strip())

#         q = list(map(int, input().rstrip().split()))

#         minimumBribes(q)


n = 5
q = [2, 1, 5, 3, 4]

resq = minimumBribes(q)

n = 5
r = [2, 5, 1, 3, 4]
resr = minimumBribes(r)