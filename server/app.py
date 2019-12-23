from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True

BOOKS = [
    {
        'title': 'The Three-Body Problem',
        'author': 'Cinxin Liu',
        'read': True
    },
    {
        'title': '1984',
        'author': 'George Orwell',
        'read': True
    },
    {
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

@app.route('/books', methods=['GET'])
def all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0')
