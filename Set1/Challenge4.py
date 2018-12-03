from Challenge123 import decode, score



f = open("Challenge4.txt", "r")

for line in f:
    result = decode(line[:-1])
    if score(result) > 28:
        print(result, score(result))

f.close()