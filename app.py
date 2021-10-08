from flask import Flask, request
import requests
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    return '', 200
@app.route('/pix', methods=['POST'])
def pix():
    requests.post('https://script.google.com/macros/s/AKfycbyZf2xDAyyUa2PJOvi8rwO1eemg04Ef6gT9jrNpTaEd0BBY0PqKdT6JbZwc05tl24Qi0Q/exec', json= request.json)
    return '', 200
"""if __name__ == '__main__':
    app.run((debug=True)"""