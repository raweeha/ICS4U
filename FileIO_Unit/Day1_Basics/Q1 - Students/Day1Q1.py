grade_9 = []
grade_10 = []
grade_11 = []
grade_12 = []

with open('allStudents.txt') as f:
    for line in f:
        line = line.strip().split('\t')
        grade = int(line[0])
        first_name = line[2].lower().title()
        last_name = line[1].lower().title()
        full_name = f'{first_name} {last_name}'

        if grade == 9:
            grade_9.append(full_name)
        elif grade == 10:
            grade_10.append(full_name)
        elif grade == 11:
            grade_11.append(full_name)
        elif grade == 12:
            grade_12.append(full_name)
                                
        
        #if line[0] == '09':
        #    grade_9.append((line[2], line[1]))
        #elif line[0] == '10':
        #    grade_10.append((line[2], line[1]))
        #elif line[0] == '11':
        #    grade_11.append((line[2], line[1]))
        #elif line[0] == '12':
        #    grade_12.append((line[2], line[1]))

print ("Grade 9:", grade_9)
print ("Grade 10:", grade_10)
print ("Grade 11:", grade_11)
print ("Grade 12:", grade_12)
