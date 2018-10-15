def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    for i, j in enumerate(plaintext):
        num = ord(j)
        if 97 <= num <= 122 or 65 <= num <= 90:
            shift = ord(keyword[i % len(keyword)])
            shift -= 97 if 97 <= num <= 122 else 65
            m = num + shift
            if 97 <= num <= 122 and m > 122:
                m -= 26
            elif 65 <= num <= 90 and m > 90:
                m -= 26
            ciphertext += chr(m)
        else:
            chiphertext += j
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    for i, j in enumerate(ciphertext):
        num = ord(j)
        if 97 <= num <= 122 or 65 <= num <= 90:
            shift = ord(keyword[i % len(keyword)])
            shift -= 97 if 97 <= num <= 122 else 65
            m = num - shift
            if 97 <= num <= 122 and m < 97:
                m += 26
            elif 65 <= num <= 90 and m < 65:
                m += 26
            plaintext += chr(m)
        else:
            plaintext += j
    return plaintext