#Create a file with 500 entries of fictitious people.
#Person ID Key, Person name, Person's occupation, Person's salary

import random

with open('occupations.txt') as f:
    occupations_list = f.read().split('\n')
    person_occupation = random.choice(occupations_list)

with open('random_names.txt') as f:
    names_list = f.read().split('\n')
    person_name = random.choice(names_list)

with open('Q1_file.txt', 'w') as file:
    

    def random_salary_generator(num):
        list_salary = []
        for i in range(500):
            salary = random.randint(25000, 125000)
            list_salary.append(f' ${salary}')
        return list_salary
        person_salary = random.choice(list_salary)

    #NNN-NN-NNNN  where N is a digit
    #for example 034-63-9543

    def random_ID_generator(num):
        list_id = []
        for i in range(0, num):
            first_group = str(random.randint(0,999)).zfill(3)
            second_group = str(random.randint(0, 99)).zfill(2)
            third_group = str(random.randint(0, 9999)).zfill(4)
            person_id = f'{first_group}-{second_group}-{third_group}'
            list_id.append(person_id)
        return list_id

    person_id = random.choice(random_ID_generator)

        
    salary_list = random_salary_generator(500)
    #print(salary_list)
    id_list = random_ID_generator(500)
    #print(id_list)

file.write(f'{person_id}, {person_name}, {person_occupation}, {person_salary}')
    


    
