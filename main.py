import random

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


message = "The river of sbou is passing and berries are growing on the floor"


def generate_cipher_alphabet(alphabet):
    cipher_alphabet = random.sample(alphabet, len(alphabet))
    return ''.join(cipher_alphabet)




def cipher(message):
    cipher_alphabet = generate_cipher_alphabet(alphabet)
    cipher = ""
    for letter in message:
        if letter.isalpha():
            letter_alphabet_index = alphabet.index(str.lower(letter))
            cipher += cipher_alphabet[letter_alphabet_index]


    return {'cipher' : cipher, 'cipher_alphabet' : cipher_alphabet}





def decipher(cipher, cipher_alphabet):
    message = ""
    for letter in cipher:
            cipher_alphabet_index = cipher_alphabet.index(str.lower(letter))
            message += alphabet[cipher_alphabet_index]

    return message


ciphered = cipher(message)


deciphered = decipher(ciphered['cipher'], ciphered['cipher_alphabet'])


print(ciphered)

print("deciphered message", deciphered)