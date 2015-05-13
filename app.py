# TODO: para cada pregunta nueva ahi que agregar en index.html una entrada nueva al form y repetir lo que se hace aqui en "paroAnswer"

import os

from flask import Flask, render_template, request, json
from flask.ext.sqlalchemy import SQLAlchemy

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "static", "numbers.json")
data = json.load(open(json_url))
ALL_STUDENT_NUMBERS = data["numbers"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:////tmp/test.db')
db = SQLAlchemy(app)

class Entry(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  studentNumber = db.Column(db.String(11), unique=True)
  paroAnswer = db.Column(db.String(2))

  def __init__(self, studentNumber, paroAnswer):
    self.studentNumber = studentNumber
    self.paroAnswer = paroAnswer

  def __repr__(self):
    return "Contestacion de - %s" % self.studentNumber

@app.route('/', methods=["GET", "POST"])
def form():
  if request.method == 'GET':
    return render_template('index.html')
  elif request.method == 'POST':
    # Get form parameters
    number = request.form.get('studentNumber', '')
    paroAnswer = request.form.get('paroAnswer', '')

    # Si el numero no esta en nuestra lista
    if number not in ALL_STUDENT_NUMBERS:
      return render_template("error.html")

    # Anadir la entrada solamente si no existe
    previousEntry = Entry.query.filter_by(studentNumber=number).first()
    if previousEntry is None:
      entry = Entry(number, paroAnswer)
      db.session.add(entry)
      db.session.commit()

    return render_template("thanks.html")

if __name__ == '__main__':
  app.run(debug=True)