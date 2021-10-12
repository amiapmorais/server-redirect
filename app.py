from flask import Flask, request
import requests
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    return '', 200
@app.route('/pix', methods=['POST'])
def pix():
    requests.post('https://script.google.com/macros/s/AKfycbxTpvi3Oe4XSD-5Iu1KHZPi_B_iiwnDyYmyM-IrFifnH-b02FyIHfMxOtFoLX8wr9WK2g/exec', json= request.json)
    return '', 200
"""if __name__ == '__main__':
    app.run((debug=True)"""