from flask import Flask, render_template, request
from random import randrange

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World!'


@app.route('/form')
def form():
   return render_template('form.html', name="Donald")


@app.route('/result', methods=['get', 'post'] )
def result():

   firstname = request.form['firstname']
   lastname = request.form['lastname']
   place = request.form['place']
   print("Firstname = " + firstname, "place = " + place)
   return "Thank you! " + firstname + " in " + place
