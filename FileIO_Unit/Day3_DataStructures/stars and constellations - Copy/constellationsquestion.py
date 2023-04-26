constellations_dict = {}
list_section = []
with open('constellations.txt') as file_in:
    for line in file_in:
        section = line.strip().split('\n', 9)
        list_section.append(section)

print(list_section)
        
    
