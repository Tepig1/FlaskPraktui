from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def http_404_handler():
    return make_response("404 Error", 400)

@app.route('/books/')
def books(genre):
    res = make_response("All Books in {} category".format(genre))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    return res