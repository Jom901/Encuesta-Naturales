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
  answer1 = db.Column(db.String(10))
  answer2 = db.Column(db.String(10))
  answer3 = db.Column(db.String(10))
  answer4 = db.Column(db.String(10))
  answer5 = db.Column(db.String(10))
  answer6 = db.Column(db.String(10))
  answer7 = db.Column(db.String(10))
  answer8 = db.Column(db.String(10))
  answer9 = db.Column(db.String(10))
  answer10 = db.Column(db.String(10))
  answer11 = db.Column(db.String(10))
  answer12 = db.Column(db.String(10))
  answer13 = db.Column(db.String(10))
  answer14 = db.Column(db.String(10))
  answer15 = db.Column(db.String(10))
  answer16 = db.Column(db.String(10))
  answer17 = db.Column(db.String(10))
  answer18 = db.Column(db.String(10))
  answer19 = db.Column(db.String(10))
  answer20 = db.Column(db.String(10))
  answer21 = db.Column(db.String(10))
  answer22 = db.Column(db.String(10))
  answer23 = db.Column(db.String(10))
  answer24 = db.Column(db.String(10))
  answer25 = db.Column(db.String(10))
  answer26 = db.Column(db.String(10))
  answer27 = db.Column(db.String(10))
  answer28 = db.Column(db.String(10))
  answer29 = db.Column(db.String(10))
  answer30 = db.Column(db.String(10))
  answer31 = db.Column(db.String(10))
  answer32 = db.Column(db.String(10))

  def __init__(self, **kwargs):
    self.studentNumber = kwargs.get("studentNumber")
    self.answer1 = kwargs.get("answer1", "n/a")
    self.answer2 = kwargs.get("answer2", "n/a")
    self.answer3 = kwargs.get("answer3", "n/a")
    self.answer4 = kwargs.get("answer4", "n/a")
    self.answer5 = kwargs.get("answer5", "n/a")
    self.answer6 = kwargs.get("answer6", "n/a")
    self.answer7 = kwargs.get("answer7", "n/a")
    self.answer8 = kwargs.get("answer8", "n/a")
    self.answer9 = kwargs.get("answer9", "n/a")
    self.answer10 = kwargs.get("answer10", "n/a")
    self.answer11 = kwargs.get("answer11", "n/a")
    self.answer12 = kwargs.get("answer12", "n/a")
    self.answer13 = kwargs.get("answer13", "n/a")
    self.answer14 = kwargs.get("answer14", "n/a")
    self.answer15 = kwargs.get("answer15", "n/a")
    self.answer16 = kwargs.get("answer16", "n/a")
    self.answer17 = kwargs.get("answer17", "n/a")
    self.answer18 = kwargs.get("answer18", "n/a")
    self.answer19 = kwargs.get("answer19", "n/a")
    self.answer20 = kwargs.get("answer20", "n/a")
    self.answer21 = kwargs.get("answer21", "n/a")
    self.answer22 = kwargs.get("answer22", "n/a")
    self.answer23 = kwargs.get("answer23", "n/a")
    self.answer24 = kwargs.get("answer24", "n/a")
    self.answer25 = kwargs.get("answer25", "n/a")
    self.answer26 = kwargs.get("answer26", "n/a")
    self.answer27 = kwargs.get("answer27", "n/a")
    self.answer28 = kwargs.get("answer28", "n/a")
    self.answer29 = kwargs.get("answer29", "n/a")
    self.answer30 = kwargs.get("answer30", "n/a")
    self.answer31 = kwargs.get("answer31", "n/a")
    self.answer32 = kwargs.get("answer32", "n/a")

  def __repr__(self):
    return "Contestacion de - %s" % self.studentNumber

@app.route('/', methods=["GET", "POST"])
def form():
  if request.method == 'GET':
    return render_template('index.html')
  elif request.method == 'POST':
    args = {}
    # Get form parameters
    number = request.form.get('studentNumber', '')

    # Si el numero no esta en nuestra lista
    if number not in ALL_STUDENT_NUMBERS:
      return render_template("error.html")

    # Anadir la entrada solamente si no existe
    previousEntry = Entry.query.filter_by(studentNumber=number).first()
    if previousEntry is None:
      args["studentNumber"] = number
      args["answer1"] = request.form.get("Answer1", "n/a")
      args["answer2"] = request.form.get("Answer2", "n/a")
      args["answer3"] = request.form.get("Answer3", "n/a")
      args["answer4"] = request.form.get("Answer4", "n/a")
      args["answer5"] = request.form.get("Answer5", "n/a")
      args["answer6"] = request.form.get("Answer6", "n/a")
      args["answer7"] = request.form.get("Answer7", "n/a")
      args["answer8"] = request.form.get("Answer8", "n/a")
      args["answer9"] = request.form.get("Answer9", "n/a")
      args["answer10"] = request.form.get("Answer10", "n/a")
      args["answer11"] = request.form.get("Answer11", "n/a")
      args["answer12"] = request.form.get("Answer12", "n/a")
      args["answer13"] = request.form.get("Answer13", "n/a")
      args["answer14"] = request.form.get("Answer14", "n/a")
      args["answer15"] = request.form.get("Answer15", "n/a")
      args["answer16"] = request.form.get("Answer16", "n/a")
      args["answer17"] = request.form.get("Answer17", "n/a")
      args["answer18"] = request.form.get("Answer18", "n/a")
      args["answer19"] = request.form.get("Answer19", "n/a")
      args["answer20"] = request.form.get("Answer20", "n/a")
      args["answer21"] = request.form.get("Answer21", "n/a")
      args["answer22"] = request.form.get("Answer22", "n/a")
      args["answer23"] = request.form.get("Answer23", "n/a")
      args["answer24"] = request.form.get("Answer24", "n/a")
      args["answer25"] = request.form.get("Answer25", "n/a")
      args["answer26"] = request.form.get("Answer26", "n/a")
      args["answer27"] = request.form.get("Answer27", "n/a")
      args["answer28"] = request.form.get("Answer28", "n/a")
      args["answer29"] = request.form.get("Answer29", "n/a")
      args["answer30"] = request.form.get("Answer30", "n/a")
      args["answer31"] = request.form.get("Answer31", "n/a")
      args["answer32"] = request.form.get("Answer32", "n/a")
      entry = Entry(**args)
      db.session.add(entry)
      db.session.commit()

    return render_template("thanks.html")

if __name__ == '__main__':
  app.run(debug=True)