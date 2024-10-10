test_array = [1,2,3,4,5]
reversed_array = list(reversed(test_array))
print(reversed_array)

def pop_highest_from(array: list):
    array_size = len(array)
    sorted_array = sorted(array)
    max_i = array_size - 1
    max = sorted_array[array_size-1]
    print(f'{sorted_array} current max is {max}')
        
    return array.pop(max_i), array
   
def quadratic(array: list):
    res = [v*v for idx, v in enumerate(array) if idx/2 <= 1]
    print(res)
    return res

# def quadratic(plot: tuple):
#     res = [(v[0]*v[0], v[1]*v[1]) for idx, v in enumerate(plot)]
#     print(res)
#     return res
            
max, array_wo_max = pop_highest_from(test_array)
print(f'the max is  {max}: {array_wo_max}')

quadratic(test_array)