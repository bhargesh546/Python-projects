
def caesar(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # shift = input("Enter the shift for the cipher: ")
    if not isinstance(shift, int) or shift < 0:
        raise ValueError("Enter a positive integer value for the shift parameter.")
    
    if not encrypt:
        shift = -shift 

    shift = shift % 26
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())

    encrypted_text = text.translate(translation_table)

    return encrypted_text

def encrypt(text, shift):
        return caesar(text, shift)

def decrypt(text, shift):
        return caesar(text, shift, encrypt=False)

encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."

decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)