import csv
import json

import requests

api_key='qAtHFCT8DKm4kkF0dKrkueifYOSUpcgNpn-FIMiPoW1BijfRT1_FUlKokalfKnDOIIPREjgwwhuytstt11DOKZbzZtKO9LJrzCpdQ0z0918PHxSr02FiE-NIfpmnXHYx'

headers = {'Authorization': 'Bearer %s' % api_key}
url='https://api.yelp.com/v3/businesses/search'
file_name = 'test.csv'
#Parameters for the get
params = {'term':'sushi','location':'Seattle'}

csv_columns = ['id','alias','name','image_url','is_closed','url','review_count','categories','rating','coordinates',
               'transactions','price','location','phone','display_phone','distance']

# Making a get request to the API
req = requests.get(url, params=params, headers=headers)

# proceed only if the status code is 200
print('The status code is {}'.format(req.status_code))

# Grabs the json data in a dictionary format.
parseddata = json.loads(req.text)
innerparse = parseddata['businesses']

# Function gets the file name of the csv file that should be used, creates headers for the file, and inputs the data in the dictionary.
with open(file_name, 'w') as file_name:
    writer = csv.DictWriter(file_name, fieldnames=csv_columns)
    writer.writeheader()
    for data in innerparse:
        writer.writerow(data)
#closes file
file_name.close()