from flask import Flask
app= Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
    #jede route braucht eigene Methode(=def)#

@app.route('/goodbye')
def goddbye():
    return 'Goddbye World!'
