from flask import request, jsonify

from myapp import app, db
from one_to_many import Person, Pet


@app.route('/')
def index():
    return "Welcome to Flask Trial"


@app.route('/add-person', methods=['POST'])
def add_person():
    person_data = request.get_json()
    person = Person(person_data['name'])
    try:
        db.session.add(person)
        db.session.commit()

        # get last inserted Person record
        person_record = db.session.query(Person).order_by(Person.id.desc()).first()

        # adding pets along with person. {"name":"Hannah", "pets":["Bella", "Lucy"]}
        if 'pets' in person_data:
            for pet in person_data['pets']:
                pet = Pet(pet, person_record.id)
                db.session.add(pet)
                db.session.commit()

        success = True
        message = 'New person with name ' + person.name + ' added successfully'
        data = {'id': person_record.id, 'name': person_record.name}
    except Exception as e:
        success = False
        message = str(e)
        data = None

    return_data = {'success': success, 'message': message, 'data': data}
    return jsonify(return_data)


@app.route('/add-pet', methods=['POST'])
def add_pet():
    pet_data = request.get_json()
    try:
        pet = Pet(pet_data['name'], pet_data['owner_id'])
        db.session.add(pet)
        db.session.commit()
        pet_record = db.session.query(Pet).order_by(Pet.id.desc()).first()
        success = True
        message = 'New pet with name ' + pet.name + ' added successfully'
        data = {'id': pet_record.id, 'name': pet_record.name}
    except Exception as e:
        success = False
        message = str(e)
        data = None

    return_data = {'success': success, 'message': message, 'data': data}
    return jsonify(return_data)


@app.route('/user/<user_id>')
def get_user(user_id):
    # get person record where id = :user_id
    #result = Person.query.filter(Person.id == user_id)

    # get all records from person table
    #result = Person.query.all()

    # select * from person join pet on person.id = pet.owner_id
    #result = Person.query.join(Pet).filter(Person.id == user_id)

    # SELECT p1.id AS person_id, p1.name AS person_name, p2.name AS pet_name
    # FROM person p1 LEFT JOIN pet p2 ON p1.id = p2.owner.id
    # WHERE p1.id = :user_id
    result = Person\
        .query\
        .with_entities(Person.id.label('person_id'), Person.name.label('person_name'), Pet.name.label('pet_name'))\
        .outerjoin(Pet)\
        .filter(Person.id == user_id)

    person = {}
    pets = []

    try:
        if result[0]:
            person = {'id': result[0].person_id, 'name': result[0].person_name}
            for row in result:
                if row.pet_name:
                    pets.append(row.pet_name)
                    person['pets'] = pets
    except:
        pass

    return jsonify(person)