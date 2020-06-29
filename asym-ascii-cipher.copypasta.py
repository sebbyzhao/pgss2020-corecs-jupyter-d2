# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
code = """
def encode_secret(secret):
    
    # Encryption key
    rotate_const = 3
    
    # Storage for encoded secret
    encoded = ""
    
    # encode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        encoded = encoded + alphabet[original_index]
        
    print(encoded)



secret = input("Please input secret to encode with hyper-premium encryption technology: ")
encode_secret(secret)
"""
exec(code)