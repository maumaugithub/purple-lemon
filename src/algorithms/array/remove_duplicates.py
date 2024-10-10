from collections import OrderedDict

def remove_duplicates(arr):
    print(set(arr))
    # Simple approach
    # arr[:] = sorted(set(arr))
    # this step removes duplicates and checks if contents are alpha string or int
    # arr[:] = sorted([c for c in set(arr) if type(c) == int or c.isalpha()])
    # This is also good but doesn't allow me to check for chars not alphabetic...
    # arr[:] = OrderedDict.fromkeys(sorted(arr))
    return len(arr), arr
    
    
demo = [8,9,8,9,5,1,1,2,1,2,3,4,5,5,5,6,7,8,9]

# res = remove_duplicates(demo)
# print(res)
# time complexity O(n)
# space complexity O(1)

# solution works for characters but doesn't know if it's non alphabetic
alpha_demo = ['z','x','c','a','a','c','b','n','n','m','r','q','/']
res_alpha = remove_duplicates(alpha_demo)
print(res_alpha)