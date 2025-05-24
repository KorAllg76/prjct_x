from flask import Flask
from flask import jsonify


import sys
import os
from pprint import pprint
pprint(sys.path)
# sys.path.append('..')
sys.path.append(os.path.join(os.getcwd(), '..'))
pprint(sys.path)
pass
app = Flask(__name__)

tutorials = [
    {
        'title': 'Video #1. Intro',
        'description': 'GET, POST routes' 
    },
    {
        'title': 'Video #2. More features',
        'description': 'PUT, DELETE routes'
    }
]

@app.route('//tutorials', methods=['GET'])
def get_list():
    return tutorials
    
if __name__ == '__main__':
    app.run(debug=True)
