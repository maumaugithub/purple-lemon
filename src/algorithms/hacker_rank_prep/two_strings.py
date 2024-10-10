
def twoStrings(s1, s2):
    if len(s2) > len(s1):
        for i in s2:
            if i in s1:
                return True
        
    return False

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     for q_itr in range(q):
#         s1 = input()

#         s2 = input()

#         result = twoStrings(s1, s2)

#         fptr.write(result + '\n')

#     fptr.close()

sample1 = 'Hello'
sample2 = 'World!! I hope you are there!'
result = twoStrings(sample1, sample2)