import csv

def create_cities_dictionary(cities_file):
    ontario_cities = {}

    with open(cities_file) as canada_cities_file:
        reader = csv.DictReader(canada_cities_file)

        for line in reader:
            if line['province_name'] == 'Ontario':
                ontario_cities[line['city']] = {'Population': int(float(line['population']))}

    return ontario_cities

def generate_properties_dictionary(property_file, ontario_cities):
    
    with open(property_file) as properties_file:
        reader = csv.DictReader(properties_file)
    
        for line in reader:
            address_parts = line['Address'].split(",")
            address_part_1 = address_parts[0].split()
            city = address_part_1[-1]
        
            if city in ontario_cities:

                properties_data = {'Address': line['Address'],
                             'Area': line['AreaName'],
                             'Price': f"${int(line['Price ($)'])}",
                             'Latitude': float(line['lat']),
                             'Longitude': float(line['lng'])}

                if 'Properties' not in ontario_cities[city]:
                    ontario_cities[city]['Properties'] = [properties_data]
                else:
                    ontario_cities[city]['Properties'].append(properties_data)
                
    return ontario_cities

def create_all_city_prices_dict(ontario_cities):
    city_prices = {}
    
    for city in ontario_cities:
        city_prices[city] = []
        if 'Properties' in ontario_cities[city]:
            for item in ontario_cities[city]['Properties']:
                city_prices[city].append(int(item['Price'].replace('$', '')))

    return city_prices


def main():
    ontario_cities = create_cities_dictionary('canadacities.csv')
    ontario_cities = generate_properties_dictionary('properties.csv', ontario_cities)
    city_prices_dict = create_all_city_prices_dict(ontario_cities)
    print(ontario_cities)
    print(city_prices_dict)

main()
