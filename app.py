from flask import Flask, request
import requests
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    return '', 200
@app.route('/pix', methods=['POST'])
def pix():
    requests.post('https://script.google.com/macros/s/AKfycbxpZj8yWx-WjVPEh-HSMiCwbij-dUS_s1dmKbfGPN-pQ88qXA6JYnkLKy27mDBVPEXgyg/exec', json= request.json)
    return '', 200
"""if __name__ == '__main__':
    app.run((debug=True)"""