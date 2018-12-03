import binascii


def repeating_key_XOR(key, string):
    """
    Encrypts a string using a 'key' using the repeating-key XOR method.
    https://en.wikipedia.org/wiki/XOR_cipher
    :param key: The key used for encoding.
    :param string: The string to be encoded
    :return: The encoded string in hex.
    """
    result = bytes( ord(key[i % len(key)]) ^ ord(j) for i,j in zip(range(len(string)), string))
    return binascii.hexlify(result)


"""
string = "Burning 'em, if you ain't quick and nimble \
I go crazy when I hear a cymbal"
key = "ICE"
print(repeating_key_XOR(key, string))
"""