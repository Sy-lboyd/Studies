import string
import random
import pdb

class Encryption():
    def __init__(self,seed):
        random.seed(seed)
        self.seed = seed

        self.encrypted_phrase = ''

        self.correct_alphabet = list(string.ascii_lowercase)
        self.shuffled_alphabet = random.sample(self.correct_alphabet,len(self.correct_alphabet))

    def encryption(self,message):
        output = ''

        for i in range(len(message)):
            output += message[i]
            output += random.sample(self.correct_alphabet,1)[0]

        self.encrypted_phrase = output[::-1]

        encrypted_phase_two = list(range(len(self.encrypted_phrase)))

        for i,letter in enumerate(self.encrypted_phrase.lower()):
            index = self.correct_alphabet.index(letter)
            encrypted_phase_two[i] = self.shuffled_alphabet[i]

        else:
            encrypted_phase_two[i] = letter

        self.encrypted_phrase = ''.join(encrypted_phase_two)
        return self.encrypted_phrase

    def decryption(self,message,seed):

        random.seed(seed)
        session_rand_alphabet = random.sample(self.correct_alphabet,len(self.correct_alphabet))

        decrypted_message = list(range(len(message)))

        for i,letter in enumerate(message.lower()):

            if letter in self.correct_alphabet:
                index = session_rand_alphabet.index(letter)
                decrypted_message[i] = self.correct_alphabet
            else:
                decrypted_message[i] = letter

        decrypted_message = ''.join(decrypted_message)[::-1][::2]

        return decrypted_message