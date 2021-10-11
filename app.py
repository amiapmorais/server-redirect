from flask import Flask, request
import requests
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    return '', 200
@app.route('/pix', methods=['POST'])
def pix():
    requests.post('https://script.google.com/macros/s/AKfycbwaN8M52aKkOogffvT460BxdN3ZjCS5fF3W0jfwgGxgv1-gwPaIsdyus60pO0gav9ggAg/exec', json= request.json)
    return '', 200
"""if __name__ == '__main__':
    app.run((debug=True)"""