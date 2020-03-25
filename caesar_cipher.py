import string

def encrypt(text,shift):
    
    #Placeholder list
    encrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase
    
    #Shifted alphabet
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half+first_half
    
    for i, letter in enumerate(text.lower()):
        
        #Letters
        if letter in alphabet:
            original_index = alphabet.index(letter)
            
            #Shifted
            new_leter = shifted_alphabet[original_index]
            
            encrypted_text[i] = new_leter
            
        #Punctiation of space    
        else:
            encrypted_text[i] = letter
            
    return ''.join(encrypted_text)
    

def decrypt(text,shift):
    decrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase

    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half+first_half
    
    for i, letter in enumerate(text.lower()):
        
        if letter in alphabet:
            original_index = alphabet.index(letter)
            
            new_leter = shifted_alphabet[original_index]
            decrypted_text[i] = new_leter
            
        else:
            decrypted_text[i] = letter
    return ''.join(decrypted_text)

def brute_force(message):
    for n in range(26):
        print("Using shift value of {}".format(n))
        print(decrypt(message,n))
        print("\n")