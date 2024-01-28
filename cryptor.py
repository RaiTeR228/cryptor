def decode(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    hackerized = 'Λß↻Ð☰∲ç╫¡¿├↑ღ∏☐þ¶┏§⊥üƴ₪✕¥ᶾ'
    
    ans = ''
    for c in s:
        try:
            ans += alphabet[hackerized.index(c)]
        except ValueError:
            ans += c
    
    return ans

def encode(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    hackerized = 'Λß↻Ð☰∲ç╫¡¿├↑ღ∏☐þ¶┏§⊥üƴ₪✕¥ᶾ'
    
    ans = ''
    for c in s:
        try:
            ans += hackerized[alphabet.index(c)]
        except ValueError:
            ans += c
    
    return ans

if __name__ == "__main__":
    while True:
        option = input("Choose an option (1 - Decode, 2 - Encode, Enter - Exit): ")
        if option == "1":
            encoded_string = input("Encoded string: ")
            print("Decoded string:", decode(encoded_string))
        elif option == "2":
            plain_string = input("Plain string: ")
            print("Encoded string:", encode(plain_string))
        else:
            break
