#!/usr/bin/env python3
#server/seed.py

from app import app
from models import db, Pet
from faker import Faker
from random import choice as ran_choice

with app.app_context():

    fake = Faker()
    Pet.query.delete()
    pets = []
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Add some Pet instances to the list
    for n in range(10):
        pets.append(Pet(name=fake.first_name(), species=ran_choice(species)))

    db.session.add_all(pets)
    db.session.commit()