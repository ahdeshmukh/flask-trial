from myapp import db


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

    def __init__(self, name, owner_id):
        self.name = name
        self.owner_id = owner_id


if __name__ == "__main__":
    db.create_all()