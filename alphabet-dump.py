# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


# dump letter/index loop
for c in alphabet:
    index = alphabet.find(c)
    print(str(index) + " => " + str(c))