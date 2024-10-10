from collections import Counter
from collections import deque

def checkMagazine(magazine, note):
    # if len(magazine) >= len(note):
    #     if note in magazine:
    #         print(f'YES')
    # elif len(note) > len(magazine):
    #     if magazine in note:
    #         print(f'YES')
        #print(f'total: {nt.total()} elem: {nt.elements}')
    mag = Counter(magazine)
    nt = Counter(note)
    # print(f'total: {mag.total()} elem: {mag.elements}')
    # print(f'total: {nt.total()} elem: {nt.elements}')
    print(f'{list(nt.elements())}')
    # if nt.elements() in mag.elements():
    #     print('YES')
    # else:
    #     print('NO')
    flag = 'Yes'
    
    for k, v in nt.items():
        print(f'{v} {mag[k]}')
        if mag.get(k,0) < v:
            flag = 'No'
            break
    print(flag)
    
    # word_count = {}
    # flag = 'Yes'
    
    # for i in magazine:
    #     if i in word_count:
    #         word_count[i] += 1
    #     else:
    #         word_count[i] = 1
    
    # for i in note:
    #     if i in word_count and word_count[i] > 0:
    #         word_count[i] -= 1
    #     else:
    #         flag = 'No'
        
    # print(flag)

# if __name__ == '__main__':
#     first_multiple_input = input().rstrip().split()

#     m = int(first_multiple_input[0])

#     n = int(first_multiple_input[1])

#     magazine = input().rstrip().split()

#     note = input().rstrip().split()

#     checkMagazine(magazine, note)

mag1 = 'give me one grand today night'
nte1 = 'give one grand today' #yes
mag2 = 'two times three is not four'
nte2 = 'two times two is four' #no
mag3 = 'ive got a lovely bunch of coconuts'
nte3 = 'ive got some coconuts' #no
mag4 = 'apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg'
nte4 = 'elo lxkvg bg mwz clm w' #yes

magazine1 = mag1.rstrip().split()
note1 = nte1.rstrip().split()
print(note1[1] in magazine1)
checkMagazine(magazine1, note1)

magazine2 = mag2.rstrip().split()
note2 = nte2.rstrip().split()
checkMagazine(magazine2, note2)

magazine3 = mag3.rstrip().split()
note3 = nte3.rstrip().split()
checkMagazine(magazine3, note3)

magazine4 = mag4.rstrip().split()
note4 = nte4.rstrip().split()
checkMagazine(magazine4, note4)