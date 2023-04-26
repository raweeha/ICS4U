def decode_phrase(some_braille, braille_dict):
    sentence = ""
    for line in some_braille:
        for letter in line:
            sentence += braille_dict[letter]
        sentence += '\n'
    return sentence

def parse_braille_file(filename):
    with open("brailledata22.txt") as f:
        braille_file = []
        for i in range (0, 5):
            full_message = []
            message = []
            for i in range(3):
                message.append(f.readline().strip())

            sentence = ""

            for i in range(0, len(message[0]), 2):
                letter = ""
                for j in range(3):
                    letter += message[j][i:i+2]

                current_message.append(letter)
            braille_file.append(current_message)
    return braille_file

def main():
    braille_to_alpha_dict = {'xooooo': 'a', 'xoxooo': 'b', 'xxoooo': 'c'

            
