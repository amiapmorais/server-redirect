from flask import Flask, request
import requests
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    return '', 200
@app.route('/pix', methods=['POST'])
def pix():
    requests.post('https://script.google.com/macros/s/AKfycby4LTY4GOntcuJoji9Z3dKowFsF5BtwmtsN29Q9YKfgwkGPui5CnD8D0kr9f-5LHY2uCQ/exec', json= request.json)
    return '', 200
"""if __name__ == '__main__':
    app.run((debug=True)"""