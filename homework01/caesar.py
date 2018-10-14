def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
def encrypt_caesar(plaintext):
    ciphertext = ""


        for i in range(len(plaintext)):
            element = plaintext[i]
                # Encrypt uppercase characters
            if (element.isupper()):
                ciphertext += chr((ord(char) + 3 - 223) % 192 + 223)

                # Encrypt lowercase characters
            else:
                ciphertext += chr((ord(char) + 3 - 255) % 224 + 255)

        return ciphertext

    plaintext = "питон"
    print
    "Text: " + plaintext
    print
    "Shift: 3"
    print
    "Cipher: " + encrypt_caesar(plaintext)


def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    return plaintext