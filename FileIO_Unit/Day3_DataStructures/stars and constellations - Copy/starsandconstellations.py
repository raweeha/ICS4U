#Complete function create_star_list(filename)
#Function returns a list of lists
#One list to store all stars, where each star is stored as a list of data
#This list is used by the application to plot each star graphically

#[x, y, z, hd, m, harv]

#Complete function create_constellations(filename)
#Function returns a dictionary of tuples
#Each unique constellation name is a key in the dictionary where
#value is the list of star pairs that comprise the constellation.

#def create_star_list(filename):
    
stars_dict = {}

with open('stars.txt') as stars_file:
    stars_file.readline()
    for line in stars_file:
        line = line.strip().split(" ",6)

        if len(line) == 7:
            data = line[0,6]
            names_list = line[6].split(';')

            for names in names_list:
                stars_dict[names] = data
#return stars_dict
            
print (stars_dict)
