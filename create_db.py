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
    peoples_table = """
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
    cur.execute(peoples_table)
    connection.commit()
    connection.close()
    print(peoples_table)
    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"

fake_data = Faker()
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
connection.close()


if __name__ == '__main__':
   main()