from cipher_functions import *


# Message to cipher
message = "The river of sbou is passing and berries are growing on the floor"

# Generates a random ciphering alphabet (You can use your own in the cipher function down below)
cipher_alphabet = generate_cipher_alphabet(alphabet)

# Ciphers a string using a cipher alphabet (I am using the generate_cipher_alphabet() to generate a random one but you can use your own)
cipher = cipher(message, cipher_alphabet)

print("Ciphered message => ", cipher)

# Deciphers a ciphered string using the cipher alphabet
deciphered = decipher(cipher, cipher_alphabet)

print("Deciphered message => ", deciphered)
