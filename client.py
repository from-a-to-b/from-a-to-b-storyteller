import json, requests

with open('example_trip.json') as f:
    tripjson = json.load(f)
    tripstr = json.dumps(tripjson)
    r = requests.post('http://127.0.0.1:5000/fictionalize', json=tripstr)
    print(r.text)