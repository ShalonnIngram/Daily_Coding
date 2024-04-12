def parse_json_list(json):
    address_list = []
    city_list = []
    state_list = []
    postal_list = []
    postal4_list = []

    # parses json data 
    address_parse = data['AddressResult']['Address']
    city_parse = data['AddressResult']['City']
    state_parse = data['AddressResult']['State']
    postal_parse = data['AddressResult']['Zip']
    postal4_parse = data['AddressResult']['Zip4']

    address_list.append(address_parse)
    city_list.append(city_parse)
    state_list.append(state_parse)
    postal_list.append(postal_parse)
    postal4_list.append(postal4_parse)

    df = pd.DataFrame(list(zip(address_list, city_list, state_list, postal_list, postal4_list)), columns=['address', 'city', 'state', 'postal', 'postal4'])
    df.to_csv('address_data.csv', index=False)
    
    return df
