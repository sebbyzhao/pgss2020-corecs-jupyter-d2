# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "_aeg\\e`aa\\bg`g\\`beg"

# Reference alphabet
# This alphabet is the same order as ASCII, but omits non-printable characters
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"



def symmetrical_rotate(string):
    """ROT47 implementation
    
    NOTE: encode and decode are the same operation in the ROT cipher family.
    """
    
    # Encryption key
    rotate_const = 47
    
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
        original_index = (index + rotate_const) % len(alphabet)
        
        # this saves each rotated letter to the output string.
        rotated = rotated + alphabet[original_index]
        
    print(rotated)



def choose_greatest():
    """Echo the largest of the two numbers given by the user to the program
    
    Warning: this function was written quickly and needs proper error handling
    """

    user_value_1 = input("What's your first number? ")
    user_value_2 = input("What's your second number? ")
    greatest_value = user_value_1 # need a value to return if 1 & 2 are equal

    if user_value_1 > user_value_2:
        greatest_value = user_value_1
    elif user_value_1 < user_value_2:
        greatest_value = user_value_2

    print( "The number with largest positive magnitude is " 
        + str(greatest_value) )



choose_greatest()