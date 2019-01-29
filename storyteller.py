from flask import Flask
from flask import request
import json
import random
import requests

# ConceptNet-related stuff
# https://github.com/commonsense/conceptnet5/wiki/API

def pick_an_english_edge(edges):
    edge = random.choice(edges)
    if edge['end']['language'] == edge['start']['language']:
        return edge
    else:
        # pick another edge if the language of start and end edges are different
        pick_an_english_edge(edges)

def pick_another_node(node, edges):
    edge = pick_an_english_edge(edges)
    try:
        if node == edge['end']['term']:
            return edge['start']['label']
        else:
            return edge['end']['label']
    except TypeError:
        # sometimes edge['end']['term'] is None? need to look into this
        pick_another_node(node, edges)

def get_something_from_conceptnet(concept):
    node = '/c/en/{}'.format(concept)
    query = ['node={}'.format(node)]
    url = 'http://api.conceptnet.io/query?{}'.format('&'.join(query))
    obj = requests.get(url).json()
    edge = pick_another_node(node, obj['edges'])
    return edge

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
    result = {'success': True, 'trip': {}, 'sequence': []}

    for key, value in data['result']['trip'].items():
        if (key != 'path'):
            result['trip'][key] = value

    for poi in data['result']['pois']:
        chunk = {'location': poi['location'], 'timestamp': poi['timestamp'], 'poi': poi, 'fiction': 'hello world'}
        result['sequence'].append(chunk) # rename. also find a way to use timestamp/loc from path and not duplicate from poi


#     for row in data:
#         row['fiction'] = 'At {timestamp}, they were passing by {POI_name}. \
# The {POI_type} felt {adjective}. \
# It also made them think about {related_concept}.'.format(
#             timestamp = row['timestamp'], 
#             POI_name=row['POI_name'], 
#             POI_type=row['POI_type'],
#             adjective=random.choice(['cool', 'boring', 'dirty', 'overrated', 'astonishing']),
#             related_concept=get_something_from_conceptnet(row['POI_type'])
#             )
    return json.dumps(result)