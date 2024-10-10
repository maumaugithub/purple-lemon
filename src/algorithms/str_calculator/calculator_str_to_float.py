# def superDigit(n, k):
#     # Write your code here

def calculator(n, k):
    # print(n*k)
    # print(sum([int(d) for d in str(n)]))
    # notice first calculate sum then times k is more efficient
    operands = n.split()
    print(f'operands {operands}')
    command_indexes = {x: [operands.index(x)] for x in "+-*/" if x in operands}
    print(f'indexes {command_indexes}')
    total = 0
    
    
    if command_indexes:
        print(operands)
        print(command_indexes)
        # return calculate_sum_of_digits(n)*k
        #total += calculate_sum_of_digits(operands, command_indexes["+"]) 
        print(total)
    else:
        total = n
    return format(int(total), ".2f")

def _find_command_indexes(operands, command_indexes):
    memo = []
    for c in command_indexes:
        found_command = operands.index(c)
        memo.append(found_command)
        # operands.pop(found_command)
        command_indexes[c] = memo
     
def add_digits(n):
    return str(n) if n <= 9 else add_digits(calculate_sum_of_digits(n))
   
def calculate_sum_of_digits(n, idx_list):
    # t = sum([int(d) for d in str(n)])

    # return sum([int(d) for d in str(n)])
    # partial = 0
    # for idx in idx_list:
    #     print(f'sum {n[idx-1:idx]} {n[idx+1:idx+2]}')
    #     partial += n[idx-1:idx] + n[idx+1:idx+2]
    return 


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = first_multiple_input[0]

#     k = int(first_multiple_input[1])

#     result = superDigit(n, k)

#     fptr.write(str(result) + '\n')

#     fptr.close()
    
n = ' 9 + 1 '.strip()

k = len(n)

result = calculator(n, k)

n2 = ' 4 '.strip()

k2 = len(n2)

result2 = calculator(n2, k2)