def cipher(text, shift, encrypt=True):
    '''
    Encrypt or decrypt of text
    :param text: a string that will be encrypted or decrypted
    :param shift: an integer that specified the shift
    :param encrypt: a boolean that indicate encrypt i.e. encrypt = True and decrypt = False
    :return: a string that has been encrypted or decrypted
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

if __name__ == "__main__":
    print(cipher("hello", 3, encrypt=True))

