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

    ciphertext = ""


        for i in range(len(plaintext)):
            element = plaintext[i]
                # uppercase characters
            if (element.isupper()):
                ciphertext += chr((ord(char) + 3 - 90 % 65 + 90)
                # lowercase characters
            else:
                ciphertext += chr((ord(char) + 3 - 122) % 97 + 122)

        return ciphertext




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