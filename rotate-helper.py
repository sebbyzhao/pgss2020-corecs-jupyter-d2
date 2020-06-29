# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"



def rotate(string, key):

    # Storage for decoded secret
    rotated = ""
    
    # decode loop
    for c in string:
    
        # find the letter in the alphabet. index is now the number that
        #   represents that letter...
        index = alphabet.find(c)
        
        # this is the meat of the cipher that adds a key value to the index.
        # The "%" operator wraps the number if it gets bigger than there are
        #   letters in the alphabet.
        original_index = (index + key) % len(alphabet)
        
        # this saves each rotated letter to the output string.
        rotated = rotated + alphabet[original_index]
        
    print(rotated)



string = str(input("Rotate what string? (Put between double quotes!) "))
key = int(input("Rotate by how much? "))

rotate(string, key)