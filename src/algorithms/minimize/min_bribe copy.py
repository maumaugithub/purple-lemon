def minimumBribes(q):
    bribes = 0

    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            # print(q[i] - (i + 1))
            print("Too chaotic")
            return
       
        for j in range(0, i):
            if q[j] > q[i]:
                bribes += 1

    print(bribes)
    return bribes

    # bribes = 0

    # for i in range(len(q)):
    #     # print(f' i is {i} item {q[i]}')
    #     if q[i] - (i + 1) > 2:
    #         print(q[i] - (i + 1))
    #         print("Too chaotic")
    #         return
    #     # print(q[i])
    #     # for j in range(max(0, q[i] - 2), i):
    #     for j in range(0, i):
    #         if q[j] > q[i]:
    #             bribes += 1

    # print(bribes)
    # return bribes
    
# if __name__ == '__main__':
#     t = int(input().strip())

#     for t_itr in range(t):
#         n = int(input().strip())

#         q = list(map(int, input().rstrip().split()))

#         minimumBribes(q)


n = 5
q = [2, 1, 5, 3, 4]

res_q = minimumBribes(q)

n = 5
r = [2, 5, 1, 3, 4]
res_r = minimumBribes(r)