def cipher(text, shift, encrypt=True):
    """
        Encrypt or decrypt of text.

        Parameters
        ----------
        text : str
          A string that will be encrypted or decrypted.
        shift : int
          An integer that specified the shift.
        encrypt : bool
          A boolean that indicate encrypt i.e. encrypt = True and decrypt = False.

        Returns
        -------
        str
          The new string that has been encrypted or decrypted.

        Examples
        --------
        >>> from cipher_ad4056 import cipher
        >>> text = "hello"
        >>> shift = 3
        >>> encrypt = True
        >>> cipher_ad4056.cipher("hello", 3, encrypt=True)
            "khoor"
        >>> from cipher_ad4056 import cipher
        >>> text = "hello"
        >>> shift = 3
        >>> encrypt = False
        >>> cipher_ad4056.cipher("hello", 3, encrypt=True)
            "ebiil"
        """
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
