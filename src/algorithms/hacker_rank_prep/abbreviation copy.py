def abbreviation(a, b):
    # Write your code here
    def abbreviation(a: str, b: str):
    bigger = Counter(b) if len(a) < len(b) else Counter(a)
    smaller = Counter(a) if len(a) < len(b) else Counter(b)
    return matchHelper(smaller, bigger)

def matchHelper(sm, bg):
    flag = 'NO'
    bag = []
    for k, v in sm.items():    
        if k.islower():
            print(f'lower {k} {v} {bg[k]}')
            if bg.get(k, 0) > 0 or bg.get(k.upper(), 0) > 0:
                bag.append(1)
        else:
            print(f'upper {k} {v} {bg[k]}')
            if bg.get(k, 0) > 0 or bg.get(k.lower(), 0) > 0:
                bag.append(1)
 
    print(sum(bag))
    return flag
