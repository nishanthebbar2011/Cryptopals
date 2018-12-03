import binascii


def score(string):
    """
    Scores the string based on the number of alphabets.
    :param string: String to be scored
    :return: Integer.
    """
    metric_array = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)] + [' ']
    answer = 0
    for i in range(len(string)):
        #print(string[i])
        if chr(string[i]) in metric_array:
            answer += 1
    #print(answer)
    return answer


def convert_hex_to_base_64(hex_string):
    """
    Converts Hex string to Base 64
    This function is the solution to Challenge 1.
    :param hex_string: String to be converted
    :return: Corresponding string in base64
    """
    #print(binascii.unhexlify(hex_string))
    return binascii.b2a_base64(binascii.unhexlify(hex_string))

#print(convert_hex_to_base_64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))


def fixed_length_XOR(hex_string1, hex_string2):
    """
    This function is the solution to Challenge2
    Performs XOR on Strings of equal length
    :param hex_string1: First Hex String
    :param hex_string2: Second Hex String
    :return: Returns the hex-encoding of the resultant string
    """
    if len(hex_string1) != len(hex_string2):
        return ""
    bin_string1 = binascii.unhexlify(hex_string1)
    bin_string2 = binascii.unhexlify(hex_string2)

    #for i, j in zip(bin_string2, bin_string1):
        #print(i^j)
    result = binascii.hexlify(bytes(c1 ^ c2 for c1, c2 in zip(bin_string1, bin_string2)))
    return result


#print(fixed_length_XOR("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))


def decode(hex_string, current_score = 0, final_result = ""):
    """
    Decodes a string which has been XOR'ed with a single character. Ranks the decoded text based on the number of alphabets.
    This function is the solution to Challenge 3
    :param hex_string: Encoded Hex String
    :param current_score: Score of the best decoding so far.
    :param final_result: Best Decoding so far.
    :return: Byte representation of the decoded text
    """
    decoded_string = binascii.unhexlify(hex_string)
    for i in range(0,256):
        result = bytes( i ^ j for j in decoded_string)
        if score(result) > current_score:
            current_score = score(result)
            final_result = result

    return final_result



#print(decode("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))