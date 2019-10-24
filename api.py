#Business Search      URL -- 'https://api.yelp.com/v3/businesses/search'
#Business Match       URL -- 'https://api.yelp.com/v3/businesses/matches'
#Phone Search         URL -- 'https://api.yelp.com/v3/businesses/search/phone'

#Business Details     URL -- 'https://api.yelp.com/v3/businesses/{id}'
#Business Reviews     URL -- 'https://api.yelp.com/v3/businesses/{id}/reviews'

#Businesses, Total, Region

# Import the modules
import requests
#from YelpAPI import get_my_key
import json

# Define a business ID
business_id = '_b_RUDVdh3IY_pNDXn2rPw'
unix_time = 1546047836

# Define my API Key, My Endpoint, and My Header
API_KEY = '4F_2Zz_KqR8W9sQGdEOr3W8kvMLHrHhjmZwaIIKWnz95thdXigFNVa6LTd7QZ0mOf8gAb4IGX_bKa-_qPBWeIW__-gTFhCdRUbwZu-jWNzTqI5PBdlI41U2W9KSvXXYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'.format(business_id)
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

# Define my parameters of the search

PARAMETERS = {'term': 'seafood',
              'location': 'Boston'}


# Make a request to the Yelp API
response = requests.get(url = ENDPOINT,
                        params = PARAMETERS,
                        headers = HEADERS)

# Conver the JSON String
business_data = response.json()

# print the response
print(json.dumps(business_data, indent = 3))

businesses = parsed["businesses"]

