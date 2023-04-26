##Read the file universityPrograms.txt and parse the data to create a
#list of lists that looks like the following.
##university_programs.txt
##
##['Ryerson', 'Toronto', 'Ontario', 'Aerospace']
##['Ryerson', 'Toronto', 'Ontario', 'Biology']
##['Ryerson', 'Toronto', 'Ontario', 'Civil Engineering']
##['Ryerson', 'Toronto', 'Ontario', 'Criminal Justice']
##['Ryerson', 'Toronto', 'Ontario', 'English']
##['Carleton', 'Ottawa', 'Ontario', 'Computer Science']
##['Carleton', 'Ottawa', 'Ontario', 'Engineering']
##['Carleton', 'Ottawa', 'Ontario', 'Industrial Design']
##['Brock', 'St. Catherines', 'Ontario', 'Accounting']
##['Brock', 'St. Catherines', 'Ontario', 'Biophysics']
##['Brock', 'St. Catherines', 'Ontario', 'Mathematics']
##['Brock', 'St. Catherines', 'Ontario', 'Nursing']


with open("universities.txt") as file:
    lines = file.readlines()

data = []
for line in lines:
    line = line.strip()
    parts = line.split(":")
    university_info = parts[0].split(", ")
    university = university_info[0]
    city = university_info[1]
    province = university_info[2]
    programs = parts[1].strip().split(" , ")
    for program in programs:
        data.append([university, city, province, program])

print(data)

























##universities_dict = {}
##
##with open('universities.txt') as file_in:
##    for line in file_in:
##        line = line.split(':')
##
##        list_programs = line[1].split(',')
##        for program in list_programs:
##            program = program.strip()
##
##            if program not in universities_dict:
##                universities_dict[line[0]] = program
##            
##                
##print(universities_dict)

##university_programs_dict = {}

##with open("university_programs.txt") as university_file:
##    for line in university_file:
##        line = line.split(":")
##
##        universities = line[0].strip().split(",  ")
##        programs = line[1].split(",")
##
##
##        for program in programs:
##            program = program.strip()
##
##            if program not in university_programs_dict:
##                university_programs_dict[program] = universities
##            else:
##                old_list = university_programs_dict[program]
##                added_list = list(dict.fromkeys(old_list + universities))
##
##                university_programs_dict[program] = added_list
##
##print(university_programs_dict["Electrical Engineering"])
##        
        
