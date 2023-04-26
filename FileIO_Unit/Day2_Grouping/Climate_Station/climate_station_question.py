#create a dictionary of all the weather stations in canada
#the dictionary should organize stations based on province
#{province:[station_name, station_name, station_name, etc), province:
#[station_name, station_name, station_name], ...} etc.

station_dict = {}

with open("climateData.csv") as climate_file:
    for i in range(32):
        climate_file.readline()

    for station in climate_file:
        line = station.strip().replace('"', "")
        stnData = line.split(",")

        if stnData[3] in station_dict:
            station_dict[stnData[3]].append(stnData[0])
        else:
            station_dict[stnData[3]] = [stnData[0]]

print(station_dict)
