import sqlite3
from tabulate import tabulate


def createDB():
    db = sqlite3.connect("mulesoft.db")
    cur = db.cursor()
    db.commit()
    db.close()


def createTable():
    db = sqlite3.connect("mulesoft.db")
    cur = db.cursor()
    try:
        cur.execute(
            "CREATE TABLE movies (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(250) NOT NULL, actor varchar(250), actress varchar(250), director varchar(250), release_year INTEGER);")
    except Exception as e:
        db.rollback()
        print("Table with this name already exists")
    finally:
        db.commit()
        db.close()


def insert(name, actor, actress, director, release_date):
    db = sqlite3.connect("mulesoft.db")
    cur = db.cursor()
    try:
        cur.execute(f"INSERT INTO movies (name, actor, actress, director, release_year) VALUES('{name}', '{actor}', '{actress}', '{director}', '{release_date}');")
        print("Data inserted Successfully!")
    except Exception as e:
        print(e)
    finally:
        db.commit()
        db.close()


def show_all():
    db = sqlite3.connect("mulesoft.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM movies")
    records = cur.fetchall()
    head = ["id", "Name", "Actor", "Actress", "Director", "Release date"]
    print("All Movies: ")
    print(tabulate(records, headers=head, tablefmt="grid"))
    db.commit()
    db.close()


def find(query):
    db = sqlite3.connect("mulesoft.db")
    cur = db.cursor()
    cur.execute(f"SELECT * FROM movies WHERE actor like '%{query}%'")
    records = cur.fetchall()
    if records:
        head = ["id", "Name", "Actor", "Actress", "Director", "Release date"]
        print("Search results: ")
        print(tabulate(records, headers=head, tablefmt="grid"))
    else:
        print("No result found")
    db.commit()
    db.close()


print("My Interesting Movies")
repeat = 1
while repeat:
    print("\n")
    print("*****MENU******")
    print("1. Create Database")
    print("2. Create Table")
    print("3. Insert a Movie")
    print("4. Show all Movies")
    print("5. Search by Actors name")
    print("6. Enter '-1' to exit")
    choice = int(input("Enter Your Choice: "))
    print("\n")
    if choice == 1:
        createDB()
    elif choice == 2:
        createTable()
    elif choice == 3:
        name = input("Enter Movie Name: ")
        actor = input("Actor Name: ")
        actress = input("Actress Name: ")
        director = input("Director Name: ")
        release_date = input("Release year in YYYY format: ")
        insert(name, actor, actress, director, release_date)
    elif choice == 4:
        show_all()
    elif choice == 5:
        query = input("Enter your query: ")
        find(query)
    elif choice == -1:
        repeat = 0
    else:
        print("Invalid Choice")
