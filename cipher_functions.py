import random

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


# Generates a random substitution cipher alphabet
def generate_cipher_alphabet(alphabet):
    cipher_alphabet = random.sample(alphabet, len(alphabet))
    return ''.join(cipher_alphabet)



# Ciphers a string using a cipher alphabet
def cipher(message, cipher_alphabet):
    cipher = ""
    for letter in message:
        if letter.isalpha():
            letter_alphabet_index = alphabet.index(str.lower(letter))
            cipher += cipher_alphabet[letter_alphabet_index]
        elif letter == ' ':
            cipher += ' '


    return cipher




# Deciphers a string using a cipher alphabet
def decipher(cipher, cipher_alphabet):
    message = ""
    for letter in cipher:
        if letter.isalpha():
            cipher_alphabet_index = cipher_alphabet.index(str.lower(letter))
            message += alphabet[cipher_alphabet_index]
        elif letter == ' ':
            message += ' '

    return message


