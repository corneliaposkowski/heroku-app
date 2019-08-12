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


@app.route('/result', methods=['get', 'post'] )
def result():

   input("Gib bitte die erste Zahl ein: ")
   zahl1 = request.form['Zahl1']
   input("Gib bitte die zweite Zahl ein: ")
   zahl2 = request.form['Zahl2']
   input("Gib bitte die Rechenart ein: ")
   rechenart = request.form['rechenart']
   print("Zahl1 = " + zahl1, "Zahl2 = " + zahl2)
   button = Button(fenster, text="Rechnen", command=action)
   button.pack()
   return "Das Ergebnis lautet " + ergebnis
