def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for character in plaintext:
        num = ord(character)
        if 97 <= num <= 122 or 65 <= num <= 90:
            coded_ch = num + 3
            if 90 < coded_ch < 97 or coded_ch > 122:
                coded_ch -= 26
            ciphertext += chr(coded_ch)
        else:
            ciphertext += character
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts chiphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for character in ciphertext:
        num = ord(character)
        if 97 <= num <= 122 or 65 <= num <= 90:
            coded_ch = num - 3
            if 90 < coded_ch < 97 or coded_ch < 65:
                coded_ch += 26
            plaintext += chr(coded_ch)
        else:
            plaintext += character

    return plaintext
