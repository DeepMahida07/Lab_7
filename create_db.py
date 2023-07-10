"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from faker import Faker
from datetime import datetime

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Creating a Table"

    connection = sqlite3.connect('social_network.db')
    cur = connection.cursor()
    create_ppl_tbl_query = """
    CREATE TABLE IF NOT EXISTS people
    (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    province TEXT NOT NULL,
    bio TEXT,
    age INTEGER,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
    );
    """
    cur.execute(create_ppl_tbl_query)
    connection.commit()
    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"

connection = sqlite3.connect('social_network.db') 
cursor = connection.cursor()
add_person_query = """
    INSERT INTO people
    (
        name,
        email,
        address,
        city,
        province,
        bio,
        age,
        created_at,
        updated_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

new_person = ('Bob Loblaw',
              'bob.loblaw@whatever.net',
              '123 Fake St.',
              'Fakesville',
              'Fake Edward Island',
              'Enjoys making funny sounds when talking.',
              46,
              datetime.now(),
              datetime.now())

cursor.execute(add_person_query, new_person)
connection.commit()

#Getting data using Faker.
fake_data = Faker()
connection = sqlite3.connect('social_network.db') 
cursor = connection.cursor()
cursor.execute(add_person_query, new_person)
for _ in range(200):
    name = fake_data.name()
    email = fake_data.email()
    address = fake_data.address().replace('\n', ', ')
    city = fake_data.city()
    province = fake_data.state()
    bio = fake_data.text(max_nb_chars=200)
    age = fake_data.random_int(min=1, max=100)
    created_at = datetime.now()
    updated_at = datetime.now()
    cursor.execute("INSERT INTO people (name, email, address, city, province, bio, age, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, email, address, city, province, bio, age, created_at, updated_at))

connection.commit()
connection.close()

if __name__ == '__main__':
   main()