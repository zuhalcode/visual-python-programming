import string

def caesar(text, shift, alphabets):
    if shift > len(alphabets):
        shift = shift % len(alphabets)
    elif shift < 0:
        shift = shift + len(alphabets)
    text = text.lower()
    text = ''.join(c for c in text if c in alphabets)
    encrypted = ''
    for c in text:
        encrypted += alphabets[(alphabets.index(c) + shift) % len(alphabets)]
    return encrypted
    
text = input("Enter the text: ")
shift = int(input("Enter the shift: "))
alphabets = string.ascii_lowercase
print(caesar(text, shift, alphabets))

