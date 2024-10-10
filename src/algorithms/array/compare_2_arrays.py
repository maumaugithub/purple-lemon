from collections import OrderedDict

def compare_two_arrays(n, m):
    if len(n) >= len(m):
        larger = OrderedDict.fromkeys(n, True)
        print('n is larger or equal')
        print(larger)
    else:
        print('m is larger')   
    

    if m in n:
        print(m)
        return True, []
    else:
        print(m)
    

demo_n = [1,2,3,4,4,7,8,9,1,10,11,12,14,15,20,20]
demo_m = [1,2,3,4,5,6]

result = compare_two_arrays(demo_n, demo_m)    