# def superDigit(n, k):
#     # Write your code here

def superDigit(n, k):
    # print(n*k)
    # print(sum([int(d) for d in str(n)]))
    # notice first calculate sum then times k is more efficient
    return add_digits(calculate_sum_of_digits(n)*k)
    
def add_digits(n):
    return str(n) if n <= 9 else add_digits(calculate_sum_of_digits(n))
   
def calculate_sum_of_digits(n):
    # t = sum([int(d) for d in str(n)])
    # print(t)
    
    return sum([int(d) for d in str(n)])


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = first_multiple_input[0]

#     k = int(first_multiple_input[1])

#     result = superDigit(n, k)

#     fptr.write(str(result) + '\n')

#     fptr.close()
    
n = '98751'

k = 4

result = superDigit(n, k)