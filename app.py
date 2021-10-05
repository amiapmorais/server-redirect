from flask import Flask, request
import requests
app = Flask(__name__)
@app.route('/pix', methods=['POST'])
def pix():
    requests.post('https://script.google.com/macros/s/AKfycbxsGXB18bwXhPoeQhRKJ2yre4ONITdXwHwjB1EBaLVcXilNTpUQechYfzO9nSRCDab0kg/exec', json= request.json)
    return '', 200
"""if __name__ == '__main__':
    app.run((debug=True)"""