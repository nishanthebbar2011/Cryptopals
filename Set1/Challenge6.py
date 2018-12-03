

def convert_string_to_binary(string):
    result = ""
    for i in string:
        result += ( bin(ord(i))[2:].zfill(8))
    return result

def hamming_distance(string1, string2):
    """
    Computes the Hamming distance between the two strings, String1 and String2
    :param string1: String 1
    :param string2: String 2
    :return: Integer, denoting the Hamming distance. -1 if the string lengths are different
    """
    if len(string1) != len(string2):
        return -1
    bin_string1 = convert_string_to_binary(string1)
    bin_string2 = convert_string_to_binary(string2)
    result = 0

    for i in range(len(bin_string1)):
        if bin_string1[i] != bin_string2[i]:
            result += 1
    return result

#print(hamming_distance("this is a test", "wokka wokka!!!"))

def guess_key_size(ciphertext, min_key_size, max_key_size):
    possible_key_size = -1
    normalized_edit_distances = []
    for i in range(min_key_size, max_key_size + 1):
        first = ciphertext[0 : i]
        second = ciphertext[i : 2 * i]
        edit_distance = hamming_distance(first, second) / i
        normalized_edit_distances.append([edit_distance, i])

    normalized_edit_distances.sort()
    result = []
    for i in range(3):
        result.append(normalized_edit_distances[i][1])
    return result



def decode_repeating_XOR(ciphertext):
    print(guess_key_size(ciphertext, 2, 40))



f = open("Challenge6.txt")
text = ""
for line in f:
    text += line[:-1]

decode_repeating_XOR(text)