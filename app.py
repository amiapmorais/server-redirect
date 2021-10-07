from flask import Flask, request
import requests
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    return '', 200
@app.route('/pix', methods=['POST'])
def pix():
    requests.post('https://script.google.com/macros/s/AKfycbwDFsfPM_brKLPcseyXTVmK3Vh3adEOyTXK2VQmaUtK2Ts00LnC8QB-6zbi3-zecFKpyg/exec', json= request.json)
    return '', 200
"""if __name__ == '__main__':
    app.run((debug=True)"""