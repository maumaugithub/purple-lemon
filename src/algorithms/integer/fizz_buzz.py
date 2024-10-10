def fizz_buzz(n):
    i = 1
    multiple_of_3 = 1
    multiple_of_5 = 1  
    while i <= n: 
       answer = ''
       is_mult_of_3 = is_multiple_of(i, 3, multiple_of_3)
       is_mult_of_5 =  is_multiple_of(i, 5, multiple_of_5)
       
       if is_mult_of_3:
           answer = 'Fizz'
           multiple_of_3 += 1
       
       if is_mult_of_5:
           answer = f'{answer}Buzz'
           multiple_of_5 += 1
       
       if not is_mult_of_3 and not is_mult_of_5:
           answer = f'{i}'
           
       print(answer)
       i += 1
       
def is_multiple_of(i, x, m):
    if i / x == m:
        return True
    return False       
        
fizz_buzz(15)