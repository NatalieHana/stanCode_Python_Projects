"""
File: caesar.py
Name: Jane
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    將cipher藉由numb來推算原始decipher
    """
    numb = int(input("Secret number: "))
    cipher = input("What's the ciphered string? ")
    cipher = cipher.upper()
    print(decipher(cipher, numb))


def decipher(cipher, numb):
    """
    :param cipher: str
    :param numb: int
    :return: str, 根據平移數(numb)所得到的解密答案
    """
    ans = ""
    for ch in cipher:
        i = ALPHABET.find(ch)
        if i == -1:
            ans += ch
        elif i+numb >= 26:
            number = i+numb-26
            ans += ALPHABET[number]
        else:
            number = i+numb
            ans += ALPHABET[number]
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
