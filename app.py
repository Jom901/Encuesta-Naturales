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
# def prepa(idString):
#   return "15" == idString.split("-")[1]

class Entry(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  studentNumber = db.Column(db.String(11), unique=True)
  answer1 = db.Column(db.String(10))
  answer2 = db.Column(db.String(10))
  answer3 = db.Column(db.String(10))
  answer4 = db.Column(db.String(10))
  answer5 = db.Column(db.String(9999))
  answer6 = db.Column(db.String(10))
  answer7 = db.Column(db.String(10))
  answer8 = db.Column(db.String(10))
  answer9 = db.Column(db.String(10))

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
      entry = Entry(**args)
      db.session.add(entry)
      db.session.commit()

    return render_template("thanks.html")

if __name__ == '__main__':
  app.run(debug=True)
  app.logger.addHandler(logging.StreamHandler(sys.stdout))
  app.logger.setLevel(logging.ERROR)