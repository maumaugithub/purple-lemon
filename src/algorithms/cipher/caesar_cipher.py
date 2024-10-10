def caesarCipher(s, k):
    if 0 <= k <= 100 and 1 <= len(s) <= 100:
        print(k % 26)
        rotation = k % 26
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        # print(alphabet[rotation:]+alphabet[:rotation])
        cipher_alphabet = alphabet[rotation:]+alphabet[:rotation]
        result = ''
        for l in s:
            if l.isalpha():
                print(l)
                if l.islower():  
                    result +=  find_and_rotate(l, alphabet, cipher_alphabet)
                else:
                    cipher_l = find_and_rotate(l.lower(), alphabet, cipher_alphabet)
                    result += cipher_l.upper()
            else:
                result += l
        return result
            
def find_and_rotate(letter, alphabet, cipher_alphabet):
    index = alphabet.find(letter) 
    return cipher_alphabet[index]
    
    
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     s = input()

#     k = int(input().strip())

#     result = caesarCipher(s, k)

#     fptr.write(result + '\n')

#     fptr.close()

s = 'middle-Outz'
k = 2
output = 'okffng-Qwvb'
# s = 'There\'s-a-starman-waiting-in-the-sky'
# k = 3
# output = 'Wkhuh\'v'

# s = '159357lcfd'
# k = 98
# output = '159357fwzx'
result = caesarCipher(s, k)