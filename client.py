import json, requests


RANDOM_TRIP_URL = 'http://localhost:8080/api/trips/random.json'
trips = requests.get(RANDOM_TRIP_URL)

with open('example_trip.json') as f:
    tripjson = json.load(f)
    tripstr = json.dumps(tripjson)
    fictionalized_trip = requests.post('http://127.0.0.1:5000/fictionalize', json=tripstr)
    print(fictionalized_trip.text)