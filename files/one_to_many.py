from flask import request, jsonify
from myapp import app, db

one_to_many_app = app


@one_to_many_app.route('/add-person', methods=['POST'])
def add_person():
    person_data = request.get_json()
    person = Person(person_data['name'])
    try:
        db.session.add(person)
        db.session.commit()
        person_record = db.session.query(Person).order_by(Person.id.desc()).first()
        success = True
        message = 'New person with name ' + person.name + ' added successfully'
        data = {'id': person_record.id, 'name': person_record.name}
    except Exception as e:
        success = False
        message = str(e)
        data = None

    return_data = {'success': success, 'message': message, 'data': data}
    return jsonify(return_data)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet', backref='owner', lazy='dynamic')

    def __init__(self, name):
        self.name = name


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))