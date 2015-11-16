# Encuesta-Naturales
A small form app created by [Christian Rodriguez](https://github.com/chrisrodz). Often times, the student senate in the
University of Puerto Rico require a website with which they can poll across the student body with official student numbers.
This small flask app helps aleviate this problem, and subsequently digitalizes all answers into a database, which can then
be datamined later on for statistics.

#The Fork

This Fork is a modification of the original model and questions posed in the form. The results will be datamined later this month.

#Requirements

As of right now, the app is intended to run on heroku. Once deployed on heroku, access heroku with

```bash
heroku run bash
```

and in the python shell run

```python
>>> from app import db
>>> db.create_all()
```
