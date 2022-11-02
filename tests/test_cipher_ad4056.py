from cipher_ad4056 import cipher_ad4056

def test_cipher():
    expected = 'khoor'
    actual = cipher_ad4056.cipher('hello', 3)
    assert actual == expected, "Result shold be " + expected

