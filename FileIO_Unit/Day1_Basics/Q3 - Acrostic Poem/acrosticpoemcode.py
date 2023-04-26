##Read the lines in from the poem in the file above.
##Print out the first letter from each line of the poem.
##Not the first letter from the character's names, but the
##first letter from each of the character's lines.
##
##It contains a hidden message called an acrostic.

message = []

with open('poem.txt') as file_in:
    for line in file_in:
        line = line.strip().split()
        first_word = (line[1])
        letter = first_word[0]
        message.append(letter)

print(message)
    
