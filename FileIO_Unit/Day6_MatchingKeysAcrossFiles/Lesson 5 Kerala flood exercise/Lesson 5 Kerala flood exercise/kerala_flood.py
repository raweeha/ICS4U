##{ district_name : { 'fatalities' : int, 'num_camps' : int,
##                    'actual_rainfall_mm' : float,
##                    'normal_rainfall_mm' : float,
##                    'no_landslides' : int,
##                    'num_damaged_houses' : int ,
##                    'warnings' : [ ] } ,
##district_wise_details

import csv

district_dict = {}

with open('district_wise_details.csv') as file_in:
    file_in.readline()
    reader = csv.reader(file_in)
    for line in reader:
        dist_name = line[0]
        fatalities = (line[1])
        num_camps = (line[2])
        actual_rain_mm = (line[3])
        normal_rain_mm = (line[4])
        no_landslides = (line[5])
        num_damaged_houses = (line[6])

        district_dict[dist_name] = {
            "Fatalities": fatalities,
            "Number of camps": num_camps,
            "Actual rain (mm)": actual_rain_mm,
            "Normal rain (mm)": normal_rain_mm,
            "Number of landslides": no_landslides,
            "Number of damaged houses": num_damaged_houses,
            "Warnings": []}

with open('warnings_actual_predicted.csv') as warnings_file:
    warnings_file.readline()
    pointer = csv.reader(warnings_file)
    for line in pointer:
        district_name = line[0]
        alert_info = line[1:]
        district_dict[district_name]["Warnings"].append(alert_info)


                
        

##        if dist_name not in district_dict:
##            district_dict[dist_name] = {}
##        district_dict[dist_name].append(fatalities, num_camps,\
##                                        actual_rain_mm, normal_rain_mm,\
##                                        no_landslides, num_damaged_houses,\
##                                        warnings)
print(district_dict)
            

    
