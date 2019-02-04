from flask import Flask
from flask import request
import json
import random
import requests

# ConceptNet-related stuff
# https://github.com/commonsense/conceptnet5/wiki/API

BAD_RELATIONS = ('/r/ExternalURL',
                '/r/EtymologicallyRelatedTo',
                '/r/EtymologicallyDerivedFrom',
                '/r/Synonym',
                '/r/FormOf',
                '/r/DerivedFrom')

def get_related_term(search_term):
    r = requests.get('http://api.conceptnet.io{}?limit=100'.format(search_term)).json()
    related_terms = [edge for edge in r['edges'] if (not edge['rel']['@id'] in BAD_RELATIONS and 
                                                     edge['end']['language'] == edge['start']['language'])]
#    # uncomment to see all edges
#     for e in related_terms:
#         print(e['start']['@id'], e['end']['@id'], e['rel'])

    random_term = random.choice(related_terms)
    if search_term in random_term['start']['@id']:
        this, that = random_term['start'], random_term['end']
    else:
        this, that = random_term['end'], random_term['start']

    return this, that

# Flask stuff

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

# The main app
# https://stackoverflow.com/questions/35661526/how-to-send-and-receive-data-from-flask

@app.route('/fictionalize', methods=['POST'])
def fictionalize():
    jsondata = request.get_json()
    data = json.loads(jsondata)

    for poi in data['pois']:
        search_term = '/c/en/'+poi['fclass']
        this, that = get_related_term(search_term)
        that, another = get_related_term(that['term'])
        adjective=random.choice(['cool', 'boring', 'dirty', 'overrated', 'astonishing'])
        poi['fiction'] = 'A {} {}. It reminded me of {} that I heard of one time. Someone had told me about {}.'.format(
            adjective, this['label'], that['label'], another['label']
            )
        # print(poi['fiction'])

    return json.dumps(data)