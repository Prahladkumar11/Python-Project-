'''It will print the country and service provider of that mobiile no.'''

import phonenumbers
from phonenumbers import geocoder, carrier

Number = input('Enter mobile No.: ')

if len(Number) == 13:
    country = phonenumbers.parse(Number, "CH")
    print(geocoder.description_for_number(country, 'en'))
    service_provider = phonenumbers.parse(Number, "en")
    print(carrier.name_for_number(service_provider, 'en'))
else:
    print('Invalid Mobile Number,   !!! Try Again !!!')
