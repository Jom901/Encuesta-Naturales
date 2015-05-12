import os

from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

ALL_STUDENT_NUMBERS = ["801-11-6705", "401-09-7818"]

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

@app.route('/')
def form():
  if request.method == 'GET':
    return render_template('index.html')
  elif request.method == 'POST':
    # Get form parameters
    number = request.form['studentNumber']
    answer = request.form['answer']

    # Si el numero no esta en nuestra lista
    if number not in ALL_STUDENT_NUMBERS:
      return render_template("error.html")

    # Añadir la entrada solamente si no existe
    previousEntry = Entry.query.filter_by(studentNumber=number).first()
    if previousEntry is None:
      entry = Entry(number, answer)
      db.session.add(entry)
      db.session.commit()

    return render_tempalte("thanks.html")




if __name__ == '__main__':
  app.run(debug=True)