def caesar_encrypt(message: str, n: int) -> str:
    """Encrypt message using caesar cipher

    :param message: message to encrypt
    :param n: shift
    :return: encrypted message
    """
    alphabet_= "abcdefghijklmnopqrstuvwxyz"
    
    i = 0
    result = ""

    while i < len(message):
        if message[i].isalpha():
            index = alphabet_.index(message[i].lower())
            new_index = (index + n) % len(alphabet_)
            if message[i].isupper():
                result += alphabet_[new_index].upper()
            else:
                result += alphabet_[new_index]
        else:
            result += message[i]
        i += 1

    return result
            



