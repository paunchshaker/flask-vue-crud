import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

BOOKS = [
    {
        'id':  uuid.uuid4().hex,
        'title': 'The Three-Body Problem',
        'author': 'Cinxin Liu',
        'read': True
    },
    {
        'id':  uuid.uuid4().hex,
        'title': '1984',
        'author': 'George Orwell',
        'read': True
    },
    {
        'id':  uuid.uuid4().hex,
        'title': 'Moby Dick',
        'author': 'Herman Melville',
        'read': False
    }
]

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id':  uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
