"""
Description:
 Prints the name and age of all people in the Social Network database
 who are age 50 or older, and saves the information to a CSV file.

Usage:
 python old_people.py
"""
import os
from create_db import db_path, script_dir
from pprint import pprint
import sqlite3
import csv


def main():
    old_people_list = get_old_people()
    print_name_and_age(old_people_list)

    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: (name, age) of old people 
    """
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Getting People Data from the Database"
    connection = sqlite3.connect('social_network.db')
    cur = connection.cursor()

    cur.execute('SELECT name, age FROM people')

    all_people = cur.fetchall()

    pprint(all_people)
    connection.commit()
    connection.close()
    return

def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    # TODO: Create function body
    # Hint: Use a for loop to iterate the list of tuples to print a sentence for each old person
    #name_and_age_list = get_old_people()
    connection = sqlite3.connect('social_network.db')
    cur = connection.cursor()
    cur.execute("SELECT name, age FROM people")
    name_and_age_list = cur.fetchall()
    
    for people in name_and_age_list:
        name, age = people
        if age >= 60:
            print(f'Person named {name} is above 60 years.')
    return

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """
    # TODO: Create function body
    # Hint: In Lab 3, we converted a list of tuples into a pandas DataFrame and saved it to a CSV file
    #csv_path = r'D:\Semester 2\Scripting Applications\Lab_7'
    connection = sqlite3.connect('social_network.db')
    cur = connection.cursor()
    cur.execute("SELECT name, age FROM people")
    name_and_age_list = cur.fetchall()

    with open(csv_path, 'w',  newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])
    for person in name_and_age_list:
            writer.writerow(person)

if __name__ == '__main__':
   main()